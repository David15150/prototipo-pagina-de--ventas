from flask import Flask, request, Response
import mysql.connector
import re
from datetime import datetime

#import winrm
#session = winrm.Session('http://localhost:5985/wsman', auth=('usuario','contraseña'))
#result = session.run_cmd('ipconfig')
#print(result.std_out.decode())


app = Flask(__name__)

def extraer_entidades(mensaje):
    resultado = {
        "fecha_reporte": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente": "No identificado",
        "tipo_incidencia": "No clasificado",
        "prioridad": "Media",
        "dispositivo": "No especificado",
        "descripcion": mensaje
    }
    
    patrones_cliente = [
        r"cliente[:\s]+([A-Za-z0-9\s]+)",
        r"de\s+([A-Za-z0-9\s]+?)(?:\s+reporta|\s+indica|\s+dice|$)",
        r"el\s+cliente\s+([A-Za-z0-9\s]+?)(?:\s+tiene|\s+reporta|$)"
    ]
    for patron in patrones_cliente:
        match = re.search(patron, mensaje, re.IGNORECASE)
        if match:
            resultado["cliente"] = match.group(1).strip().capitalize()
            break
    
    incidencias_keywords = {
        "DVR": ["dvr", "grabadora", "no graba", "no enciende dvr"],
        "Cámara": ["cámara", "camara", "no se ve", "imagen negra"],
        "Red": ["red", "wifi", "internet", "conexión", "offline"],
        "Software": ["software", "aplicación", "app", "no abre"],
    }
    mensaje_lower = mensaje.lower()
    for tipo, keywords in incidencias_keywords.items():
        for kw in keywords:
            if kw in mensaje_lower:
                resultado["tipo_incidencia"] = tipo
                break
        if resultado["tipo_incidencia"] != "No clasificado":
            break
    
    prioridad_alta = ["urgente", "emergencia", "inmediato", "crítico"]
    prioridad_baja = ["consulta", "duda", "sin urgencia"]
    for palabra in prioridad_alta:
        if palabra in mensaje_lower:
            resultado["prioridad"] = "Alta"
            break
    for palabra in prioridad_baja:
        if palabra in mensaje_lower:
            resultado["prioridad"] = "Baja"
            break
    
    return resultado

def insertar_en_mysql(resultado):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="",    
        database="soportes_tecnicos"
    )
    cursor = conn.cursor()
    
    # Buscar o insertar cliente
    cursor.execute("SELECT id_cliente FROM clientes WHERE nombre = %s", (resultado["cliente"],))
    cliente = cursor.fetchone()
    if cliente:
        id_cliente = cliente[0]
    else:
        cursor.execute("INSERT INTO clientes (nombre) VALUES (%s)", (resultado["cliente"],))
        id_cliente = cursor.lastrowid
        conn.commit()
    
    # Insertar incidencia
    query = """INSERT INTO incidencias (id_cliente, tipo_incidencia, descripcion, fecha_reporte, estado)
               VALUES (%s, %s, %s, NOW(), 'pendiente')"""
    cursor.execute(query, (id_cliente, resultado["tipo_incidencia"], resultado["descripcion"]))
    conn.commit()
    
    cursor.close()
    conn.close()
    print(" Datos insertados en MySQL correctamente")

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    mensaje = request.form.get("Body", "")
    remitente = request.form.get("From", "")
    print(f"Mensaje recibido de {remitente}: {mensaje}")
    
    resultado = extraer_entidades(mensaje)
    insertar_en_mysql(resultado)
    
    respuesta = f" Incidencia registrada. Tipo: {resultado['tipo_incidencia']}. Prioridad: {resultado['prioridad']}."
    return Response(respuesta, mimetype="text/plain")

if __name__ == "__main__":
    app.run(port=5000)