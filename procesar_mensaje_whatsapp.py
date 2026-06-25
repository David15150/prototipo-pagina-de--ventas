import re
import datetime
from datetime import datetime

# ==============================================
# SIMULADOR DE PROCESAMIENTO DE MENSAJE DE WHATSAPP
# Para evidencia de prácticas profesionales
# Extrae: fecha, cliente, tipo de incidencia, prioridad
# ==============================================

def extraer_entidades(mensaje):
    """
    Extrae información estructurada de un mensaje de WhatsApp
    usando expresiones regulares y palabras clave
    """
    
    # Inicializar resultado
    resultado = {
        "fecha_reporte": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cliente": "No identificado",
        "tipo_incidencia": "No clasificado",
        "prioridad": "Media",
        "dispositivo": "No especificado",
        "descripcion": mensaje
    }
    
    # 1. EXTRAER CLIENTE (buscar palabras clave o patrones)
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
    
    # Si no se encontró cliente por patrón, buscar palabra que parezca empresa o nombre
    if resultado["cliente"] == "No identificado":
        palabras = mensaje.split()
        for p in palabras[:5]:  # primeras 5 palabras
            if len(p) > 4 and p[0].isupper():
                resultado["cliente"] = p
                break
    
    # 2. EXTRAER TIPO DE INCIDENCIA
    incidencias_keywords = {
        "DVR": ["dvr", "grabadora", "no graba", "no enciende dvr"],
        "Cámara": ["cámara", "camara", "no se ve", "imagen negra", "pixeles", "camara ip"],
        "Red": ["red", "wifi", "internet", "conexión", "offline", "sin red"],
        "Software": ["software", "aplicación", "app", "no abre", "error app", "plataforma"],
        "Acceso": ["acceso", "usuario", "contraseña", "login", "no entra"],
        "Almacenamiento": ["disco duro", "almacenamiento", "hd", "no graba", "disco lleno"]
    }
    
    mensaje_lower = mensaje.lower()
    for tipo, keywords in incidencias_keywords.items():
        for kw in keywords:
            if kw in mensaje_lower:
                resultado["tipo_incidencia"] = tipo
                break
        if resultado["tipo_incidencia"] != "No clasificado":
            break
    
    # 3. EXTRAER DISPOSITIVO (modelo o referencia)
    patrones_dispositivo = [
        r"dispositivo[:\s]+([A-Za-z0-9\-\s]+)",
        r"equipo[:\s]+([A-Za-z0-9\-\s]+)",
        r"([A-Za-z0-9\-]+\s+[Dd]ahua|[Hh]ikvision|[Dd]vr|[Cc]ámara)"
    ]
    
    for patron in patrones_dispositivo:
        match = re.search(patron, mensaje, re.IGNORECASE)
        if match:
            resultado["dispositivo"] = match.group(1).strip()
            break
    
    # 4. DETERMINAR PRIORIDAD según palabras clave
    prioridad_alta = ["urgente", "emergencia", "inmediato", "caída total", "no funciona nada", "crítico", "se quema"]
    prioridad_baja = ["consulta", "duda", "pregunta", "cuando puedas", "sin urgencia", "eventualmente"]
    
    for palabra in prioridad_alta:
        if palabra in mensaje_lower:
            resultado["prioridad"] = "Alta"
            break
    
    for palabra in prioridad_baja:
        if palabra in mensaje_lower:
            resultado["prioridad"] = "Baja"
            break
    
    return resultado


def mostrar_resultado(resultado):
    """
    Muestra el resultado formateado en consola (para la evidencia)
    """
    print("\n" + "="*60)
    print("📱 PROCESAMIENTO DE MENSAJE DE WHATSAPP - SISTEMA DE EXTRACCIÓN IA")
    print("="*60)
    print(f"\n📅 Fecha y hora de reporte: {resultado['fecha_reporte']}")
    print(f"🏢 Cliente: {resultado['cliente']}")
    print(f"🔧 Tipo de incidencia: {resultado['tipo_incidencia']}")
    print(f"⚡ Prioridad: {resultado['prioridad']}")
    print(f"📟 Dispositivo afectado: {resultado['dispositivo']}")
    print(f"\n📝 Descripción original: {resultado['descripcion']}")
    print("\n" + "="*60)
    print("✅ EXTRACCIÓN COMPLETADA - Datos listos para insertar en MySQL")
    print("="*60 + "\n")


# ==============================================
# MENSAJES DE PRUEBA (simulan lo que llega por WhatsApp)
# ==============================================

mensajes_prueba = [
    "Cliente: Empresa Seguridad Total, reporta que el DVR Hikvision DS-7216 no enciende desde esta mañana. Urgente.",
    
    "El cliente ElectroSur reporta falla en cámara IP Dahura, no se ve imagen, solo pantalla negra. Revisar con prioridad.",
    
    "Consultoría Jurídica del Valle indica que su software de monitoreo no abre, da error de conexión. ¿Podrían revisar sin urgencia?",
    
    "URGENTE: Cliente Supermercado El Ahorro - caída total del sistema de videovigilancia, no graba ningún canal. Se requiere atención inmediata.",
    
    "Hotel Estelar reporta que la red de cámaras está intermitente, se pierde señal cada 5 minutos."
]

# ==============================================
# EJECUCIÓN PRINCIPAL
# ==============================================

if __name__ == "__main__":
    print("\n🚀 INICIANDO SISTEMA DE PROCESAMIENTO DE SOPORTES TÉCNICOS")
    print("🤖 Motor de extracción NLP - Prácticas Profesionales Ingeniería de Sistemas")
    print("📡 Simulando recepción de mensajes desde grupo de WhatsApp...\n")
    
    # Procesar cada mensaje de prueba
    for i, mensaje in enumerate(mensajes_prueba, 1):
        print(f"\n{'─'*60}")
        print(f"📨 MENSAJE #{i} RECIBIDO")
        print(f"{'─'*60}")
        print(f"Mensaje original: {mensaje}")
        
        # Extraer entidades
        resultado = extraer_entidades(mensaje)
        
        # Mostrar resultado formateado
        mostrar_resultado(resultado)
        
        input("Presiona ENTER para procesar el siguiente mensaje...")
    
    print("\n🎉 PROCESAMIENTO COMPLETADO")
    print("Los datos extraídos pueden ser insertados automáticamente en MySQL.")