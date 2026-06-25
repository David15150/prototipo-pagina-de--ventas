<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ProAcademy — Cursos, Servicios y Soluciones</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#04101F;
  --s1:#0A1E35;
  --s2:#102840;
  --s3:#1A3553;
  --teal:#00D4AA;
  --teal-d:rgba(0,212,170,0.12);
  --teal-b:rgba(0,212,170,0.28);
  --amber:#F59E0B;
  --t1:#EEF4FA;
  --t2:#7FAABF;
  --t3:#3D5F78;
  --border:rgba(255,255,255,0.07);
  --bactive:rgba(0,212,170,0.28);
}
html{scroll-behavior:smooth}
body{font-family:'DM Sans',system-ui,sans-serif;background:var(--bg);color:var(--t1);min-height:100vh;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
button{font-family:inherit}

/* ── NAV ── */
nav{position:sticky;top:0;z-index:100;background:rgba(4,16,31,0.88);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border-bottom:1px solid var(--border)}
.nav-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;gap:2rem;height:64px;padding:0 2rem}
.logo{font-family:'DM Serif Display',serif;font-size:1.45rem;flex-shrink:0}
.logo span{color:var(--teal)}
.nav-links{display:flex;gap:1.75rem;list-style:none;margin-left:auto}
.nav-links a{font-size:.85rem;color:var(--t2);transition:color .2s}
.nav-links a:hover{color:var(--t1)}
.nav-right{display:flex;align-items:center;gap:.75rem;flex-shrink:0}
.cart-btn{position:relative;background:var(--s2);border:1px solid var(--border);color:var(--t1);padding:.45rem 1rem;border-radius:8px;cursor:pointer;display:flex;align-items:center;gap:7px;font-size:.85rem;transition:border-color .2s}
.cart-btn:hover{border-color:var(--bactive)}
.cart-count{background:var(--teal);color:#04101F;font-size:.65rem;font-weight:700;width:17px;height:17px;border-radius:50%;display:flex;align-items:center;justify-content:center;transition:transform .3s}
.cart-count.bump{transform:scale(1.4)}
.btn-cta{background:var(--teal);color:#04101F;border:none;padding:.45rem 1.2rem;border-radius:8px;cursor:pointer;font-size:.85rem;font-weight:600;transition:opacity .2s}
.btn-cta:hover{opacity:.88}

/* ── HERO ── */
.hero{max-width:1200px;margin:0 auto;padding:5rem 2rem 4rem;text-align:center}
.eyebrow{display:inline-block;background:var(--teal-d);border:1px solid var(--teal-b);color:var(--teal);font-size:.7rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;padding:.3rem 1rem;border-radius:100px;margin-bottom:1.5rem}
.hero h1{font-family:'DM Serif Display',serif;font-size:clamp(2.4rem,5.5vw,3.8rem);line-height:1.1;color:var(--t1);margin-bottom:1.2rem}
.hero h1 em{color:var(--teal);font-style:normal}
.hero-sub{font-size:1.05rem;color:var(--t2);max-width:560px;margin:0 auto 2.5rem;line-height:1.65}
.search-wrap{display:flex;max-width:520px;margin:0 auto}
.search-wrap input{flex:1;background:var(--s1);border:1px solid var(--border);border-right:none;color:var(--t1);padding:.85rem 1.25rem;border-radius:10px 0 0 10px;font-size:.875rem;outline:none;transition:border-color .2s}
.search-wrap input::placeholder{color:var(--t3)}
.search-wrap input:focus{border-color:var(--bactive)}
.search-wrap button{background:var(--teal);color:#04101F;border:none;padding:.85rem 1.5rem;border-radius:0 10px 10px 0;cursor:pointer;font-weight:600;font-size:.875rem;transition:opacity .2s}
.search-wrap button:hover{opacity:.88}
.stats{display:flex;justify-content:center;gap:3rem;margin-top:3rem;padding-top:2.5rem;border-top:1px solid var(--border);flex-wrap:wrap;gap:2rem}
.stat-n{font-family:'DM Serif Display',serif;font-size:2rem}
.stat-n span{color:var(--teal)}
.stat-l{font-size:.75rem;color:var(--t2);margin-top:.2rem}

/* ── CATALOG ── */
.catalog{max-width:1200px;margin:0 auto;padding:0 2rem 4.5rem}
.tabs{display:flex;border-bottom:1px solid var(--border);margin-bottom:2rem;gap:.25rem;overflow-x:auto}
.tab-btn{background:none;border:none;color:var(--t3);font-size:.9rem;font-weight:500;padding:.7rem 1.2rem;cursor:pointer;position:relative;transition:color .2s;white-space:nowrap}
.tab-btn:hover{color:var(--t2)}
.tab-btn.active{color:var(--teal)}
.tab-btn.active::after{content:'';position:absolute;bottom:-1px;left:0;right:0;height:2px;background:var(--teal);border-radius:2px 2px 0 0}
.panel{display:none}
.panel.active{display:block}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1.2rem}

/* ── CARDS ── */
.card{background:var(--s1);border:1px solid var(--border);border-radius:12px;overflow:hidden;transition:border-color .25s,transform .25s}
.card:hover{border-color:var(--bactive);transform:translateY(-3px)}
.card-vis{height:130px;display:flex;align-items:center;justify-content:center;font-size:2.5rem;position:relative}
.cv-teal{background:linear-gradient(135deg,#031E18,#093E2E)}
.cv-blue{background:linear-gradient(135deg,#031428,#0A2240)}
.cv-purple{background:linear-gradient(135deg,#130528,#1E0840)}
.cv-amber{background:linear-gradient(135deg,#201505,#3A230A)}
.badge{position:absolute;top:10px;left:10px;font-size:.62rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;padding:3px 8px;border-radius:100px;border:1px solid;background:rgba(4,16,31,.5)}
.badge-new{border-color:var(--teal);color:var(--teal)}
.badge-hot{border-color:var(--amber);color:var(--amber)}
.badge-corp{border-color:#a78bfa;color:#a78bfa}
.card-body{padding:1.15rem}
.card-body h3{font-size:.9rem;font-weight:600;line-height:1.4;margin-bottom:.4rem}
.card-body p{font-size:.77rem;color:var(--t2);line-height:1.5;margin-bottom:.85rem}
.tags{display:flex;align-items:center;gap:.4rem;flex-wrap:wrap;margin-bottom:.85rem}
.tag{background:var(--s2);color:var(--t3);font-size:.67rem;padding:2px 7px;border-radius:100px;border:1px solid var(--border)}
.stars{display:flex;align-items:center;gap:3px;font-size:.72rem;color:var(--amber);margin-left:auto}
.card-foot{display:flex;align-items:flex-end;justify-content:space-between;gap:.5rem}
.price-old{font-size:.72rem;color:var(--t3);text-decoration:line-through;display:block}
.price-main{font-family:'DM Serif Display',serif;font-size:1.35rem}
.price-cur{font-family:'DM Sans',sans-serif;font-size:.72rem;color:var(--t2);font-weight:400}
.add-btn{background:var(--teal-d);border:1px solid var(--teal-b);color:var(--teal);padding:.4rem .9rem;border-radius:8px;cursor:pointer;font-size:.78rem;font-weight:600;transition:background .2s,color .2s;white-space:nowrap}
.add-btn:hover{background:var(--teal);color:#04101F}

/* ── BANNER ── */
.banner{max-width:1200px;margin:0 auto;padding:0 2rem 4rem}
.banner-inner{background:linear-gradient(120deg,#051928,#0A2A20);border:1px solid var(--bactive);border-radius:16px;padding:2.25rem 2.5rem;display:flex;align-items:center;justify-content:space-between;gap:2rem;flex-wrap:wrap}
.banner-ey{color:var(--teal);font-size:.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;margin-bottom:.65rem}
.banner-inner h2{font-family:'DM Serif Display',serif;font-size:1.65rem;margin-bottom:.6rem}
.banner-inner p{font-size:.85rem;color:var(--t2);max-width:380px}
.banner-price-wrap{text-align:right}
.banner-price{font-family:'DM Serif Display',serif;font-size:2.75rem;color:var(--teal)}
.banner-plabel{font-size:.75rem;color:var(--t2);margin-bottom:.9rem}
.banner-old{font-size:.8rem;color:var(--t3);text-decoration:line-through;margin-bottom:.25rem}

/* ── PAYMENT ── */
.paysec{max-width:1200px;margin:0 auto;padding:0 2rem 5rem}
.sec-head{text-align:center;margin-bottom:2.25rem}
.sec-head h2{font-family:'DM Serif Display',serif;font-size:1.9rem;margin-bottom:.4rem}
.sec-head p{color:var(--t2);font-size:.875rem}
.trust{display:flex;justify-content:center;gap:1.75rem;flex-wrap:wrap;margin-bottom:2rem}
.tbadge{display:flex;align-items:center;gap:.45rem;font-size:.78rem;color:var(--t2)}
.ticon{width:24px;height:24px;background:var(--s2);border:1px solid var(--border);border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:.75rem}
.pay-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(148px,1fr));gap:.9rem}
.pay-card{background:var(--s1);border:1px solid var(--border);border-radius:12px;padding:1.35rem .85rem;text-align:center;transition:border-color .2s}
.pay-card:hover{border-color:rgba(255,255,255,.15)}
.pay-icon{width:46px;height:46px;border-radius:10px;display:flex;align-items:center;justify-content:center;margin:0 auto .7rem;font-size:.78rem;font-weight:800;letter-spacing:-.02em}
.pi-pse{background:#1434CB;color:#fff}
.pi-nequi{background:#7B2FBE;color:#fff}
.pi-davi{background:#ED1C24;color:#fff}
.pi-efecty{background:#F9A200;color:#000}
.pi-visa{background:#1A1F71;color:#fff;font-style:italic;font-size:.88rem;letter-spacing:.03em}
.pi-mc{background:linear-gradient(90deg,#EB001B 40%,#F79E1B);color:#fff;font-size:.65rem}
.pi-pp{background:#003087;color:#fff;font-size:.68rem}
.pay-name{font-size:.82rem;font-weight:500;margin-bottom:.2rem}
.pay-desc{font-size:.68rem;color:var(--t3)}

/* ── MODAL ── */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.72);-webkit-backdrop-filter:blur(5px);backdrop-filter:blur(5px);z-index:999;align-items:center;justify-content:center;padding:1rem}
.overlay.open{display:flex}
.modal{background:var(--s1);border:1px solid var(--bactive);border-radius:16px;width:100%;max-width:500px;max-height:88vh;overflow-y:auto;animation:up .28s ease}
@keyframes up{from{transform:translateY(22px);opacity:0}to{transform:translateY(0);opacity:1}}
.modal-h{padding:1.4rem 1.65rem;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between}
.modal-h h3{font-family:'DM Serif Display',serif;font-size:1.2rem}
.close-btn{background:none;border:none;color:var(--t3);font-size:1.3rem;cursor:pointer;line-height:1;transition:color .2s}
.close-btn:hover{color:var(--t1)}
.modal-b{padding:1.4rem 1.65rem}
.ci{display:flex;align-items:center;gap:.75rem;padding:.7rem 0;border-bottom:1px solid var(--border)}
.ci:last-child{border-bottom:none}
.ci-emo{width:36px;height:36px;background:var(--s2);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;flex-shrink:0}
.ci-info{flex:1}
.ci-info h4{font-size:.82rem;font-weight:500}
.ci-info p{font-size:.72rem;color:var(--t2);margin-top:1px}
.ci-price{font-weight:600;font-size:.9rem;color:var(--teal);white-space:nowrap}
.rm-btn{background:none;border:none;color:var(--t3);cursor:pointer;font-size:.85rem;padding:4px;transition:color .2s}
.rm-btn:hover{color:#f56565}
.empty-cart{text-align:center;padding:2.5rem 0;color:var(--t3);font-size:.875rem}
.cart-total-row{display:flex;justify-content:space-between;align-items:baseline;padding:.9rem 0 0;border-top:1px solid var(--border);margin-top:.5rem}
.ct-label{font-size:.85rem;color:var(--t2)}
.ct-amount{font-family:'DM Serif Display',serif;font-size:1.5rem;color:var(--teal)}

/* checkout steps */
.step{display:none}
.step.on{display:block}
.step-title{font-size:.78rem;font-weight:600;color:var(--t2);letter-spacing:.06em;text-transform:uppercase;margin-bottom:1rem}
.frow{margin-bottom:.9rem}
.frow label{display:block;font-size:.77rem;color:var(--t2);margin-bottom:5px}
.frow input,.frow select{width:100%;background:var(--s2);border:1px solid var(--border);color:var(--t1);padding:.7rem 1rem;border-radius:8px;font-size:.85rem;font-family:inherit;outline:none;transition:border-color .2s}
.frow input:focus,.frow select:focus{border-color:var(--bactive)}
.frow select option{background:var(--s2)}
.half{display:grid;grid-template-columns:1fr 1fr;gap:.75rem}
.pm-pick{display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-bottom:1rem}
.pm-opt{background:var(--s2);border:1px solid var(--border);border-radius:8px;padding:.55rem .75rem;cursor:pointer;display:flex;align-items:center;gap:.5rem;font-size:.8rem;color:var(--t2);transition:border-color .2s,color .2s;-webkit-user-select:none;user-select:none}
.pm-opt.sel{border-color:var(--bactive);color:var(--teal)}
.pm-ring{width:9px;height:9px;border-radius:50%;border:1.5px solid currentColor;flex-shrink:0;transition:background .2s}
.pm-opt.sel .pm-ring{background:var(--teal)}
.cc-fields{display:none;margin-top:.75rem}
.cc-fields.show{display:block}
.success-wrap{text-align:center;padding:1.5rem 0}
.suc-ico{width:62px;height:62px;background:var(--teal-d);border:2px solid var(--teal);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.8rem;margin:0 auto 1.1rem}
.success-wrap h3{font-family:'DM Serif Display',serif;font-size:1.45rem;margin-bottom:.5rem}
.success-wrap p{color:var(--t2);font-size:.85rem;line-height:1.6}
.modal-f{padding:.85rem 1.65rem 1.4rem;display:flex;gap:.65rem}
.btn-back{flex:1;background:none;border:1px solid var(--border);color:var(--t2);padding:.7rem;border-radius:8px;cursor:pointer;font-size:.85rem;transition:border-color .2s,color .2s}
.btn-back:hover{border-color:rgba(255,255,255,.2);color:var(--t1)}
.btn-go{flex:2;background:var(--teal);color:#04101F;border:none;padding:.7rem;border-radius:8px;cursor:pointer;font-size:.875rem;font-weight:600;transition:opacity .2s}
.btn-go:hover{opacity:.88}

/* ── FOOTER ── */
footer{border-top:1px solid var(--border);padding:2rem 2rem}
.foot-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:1.5rem;flex-wrap:wrap}
.foot-logo{font-family:'DM Serif Display',serif;font-size:1.1rem}
.foot-logo span{color:var(--teal)}
.foot-links{display:flex;gap:1.75rem;list-style:none;flex-wrap:wrap}
.foot-links a{font-size:.78rem;color:var(--t3);transition:color .2s}
.foot-links a:hover{color:var(--t2)}
.foot-copy{font-size:.75rem;color:var(--t3)}

/* Toast */
.toast{position:fixed;bottom:1.75rem;right:1.75rem;background:var(--s2);border:1px solid var(--bactive);color:var(--t1);padding:.8rem 1.15rem;border-radius:10px;font-size:.83rem;z-index:2000;display:flex;align-items:center;gap:.5rem;transform:translateY(80px);opacity:0;transition:all .3s;pointer-events:none}
.toast.show{transform:translateY(0);opacity:1}
.toast-dot{width:7px;height:7px;background:var(--teal);border-radius:50%;flex-shrink:0}
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <div class="logo">Pro<span>Academy</span></div>
    <ul class="nav-links">
      <li><a href="#cursos">Cursos</a></li>
      <li><a href="#servicios">Servicios</a></li>
      <li><a href="#soluciones">Soluciones</a></li>
      <li><a href="#pago">Métodos de pago</a></li>
    </ul>
    <div class="nav-right">
      <button class="cart-btn" onclick="openCart()">
        🛒 Carrito
        <span class="cart-count" id="cartCount">0</span>
      </button>
      <button class="btn-cta" onclick="openCart()">Comprar ahora</button>
    </div>
  </div>
</nav>

<!-- HERO -->
<section class="hero">
  <div class="eyebrow">🇨🇴 &nbsp; Aprende · Crece · Transforma</div>
  <h1>Conocimiento que <em>impulsa</em><br>tu empresa al siguiente nivel</h1>
  <p class="hero-sub">Cursos especializados, folletos profesionales, servicios de consultoría y soluciones digitales para empresas colombianas.</p>
  <div class="search-wrap">
    <input type="text" placeholder="Buscar cursos, servicios o soluciones…" id="searchInput" onkeydown="if(event.key==='Enter')searchProducts()">
    <button onclick="searchProducts()">Buscar</button>
  </div>
  <div class="stats">
    <div><div class="stat-n"><span>+2.400</span></div><div class="stat-l">Estudiantes activos</div></div>
    <div><div class="stat-n"><span>96%</span></div><div class="stat-l">Satisfacción</div></div>
    <div><div class="stat-n"><span>38</span></div><div class="stat-l">Productos disponibles</div></div>
    <div><div class="stat-n"><span>7</span></div><div class="stat-l">Métodos de pago</div></div>
  </div>
</section>

<!-- CATALOG -->
<section class="catalog" id="cursos">
  <div class="tabs">
    <button class="tab-btn active" onclick="showTab('cursos',this)">📚 Cursos</button>
    <button class="tab-btn" onclick="showTab('folletos',this)">📄 Folletos y Plantillas</button>
    <button class="tab-btn" onclick="showTab('servicios',this)" id="tab-servicios">🎯 Servicios</button>
    <button class="tab-btn" onclick="showTab('soluciones',this)" id="tab-soluciones">⚙️ Soluciones Empresariales</button>
  </div>

  <!-- CURSOS -->
  <div class="panel active grid" id="panel-cursos">
    <div class="card">
      <div class="card-vis cv-teal"><span>📊</span><span class="badge badge-hot">Popular</span></div>
      <div class="card-body">
        <h3>Excel Avanzado para Negocios</h3>
        <p>Tablas dinámicas, macros, Power Query y dashboards para tomar decisiones con datos.</p>
        <div class="tags"><span class="tag">48 horas</span><span class="tag">Certificado</span><span class="stars">★★★★★ 4.9</span></div>
        <div class="card-foot">
          <div><span class="price-old">$129.000</span><span class="price-main">$89.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Excel Avanzado para Negocios','$89.000',89000,'📊')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-blue"><span>📱</span><span class="badge badge-new">Nuevo</span></div>
      <div class="card-body">
        <h3>Marketing Digital & SEO Práctico</h3>
        <p>Google Ads, Meta Ads, SEO técnico y analítica web para hacer crecer tu negocio online.</p>
        <div class="tags"><span class="tag">60 horas</span><span class="tag">Proyectos reales</span><span class="stars">★★★★★ 4.8</span></div>
        <div class="card-foot">
          <div><span class="price-old">$180.000</span><span class="price-main">$129.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Marketing Digital & SEO','$129.000',129000,'📱')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-purple"><span>🤖</span><span class="badge badge-new">Nuevo</span></div>
      <div class="card-body">
        <h3>Gestión de Proyectos con IA</h3>
        <p>PMI, metodologías ágiles y herramientas de inteligencia artificial para liderar equipos.</p>
        <div class="tags"><span class="tag">36 horas</span><span class="tag">Scrum</span><span class="stars">★★★★☆ 4.7</span></div>
        <div class="card-foot">
          <div><span class="price-main">$149.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Gestión de Proyectos con IA','$149.000',149000,'🤖')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-amber"><span>📈</span><span class="badge badge-hot">Popular</span></div>
      <div class="card-body">
        <h3>Power BI para Análisis Empresarial</h3>
        <p>Conecta fuentes de datos, crea visualizaciones y comparte reportes interactivos en tu empresa.</p>
        <div class="tags"><span class="tag">40 horas</span><span class="tag">Power BI</span><span class="stars">★★★★★ 5.0</span></div>
        <div class="card-foot">
          <div><span class="price-old">$160.000</span><span class="price-main">$119.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Power BI Empresarial','$119.000',119000,'📈')">+ Añadir</button>
        </div>
      </div>
    </div>
  </div>

  <!-- FOLLETOS -->
  <div class="panel grid" id="panel-folletos">
    <div class="card">
      <div class="card-vis cv-teal"><span>🗂️</span><span class="badge badge-hot">Popular</span></div>
      <div class="card-body">
        <h3>Pack de Plantillas Corporativas (50 diseños)</h3>
        <p>Propuestas, actas, contratos, informes y presentaciones con identidad profesional lista para usar.</p>
        <div class="tags"><span class="tag">Word + PPT</span><span class="tag">Editable</span><span class="stars">★★★★★ 4.9</span></div>
        <div class="card-foot">
          <div><span class="price-old">$75.000</span><span class="price-main">$45.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Pack Plantillas Corporativas','$45.000',45000,'🗂️')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-blue"><span>🎨</span></div>
      <div class="card-body">
        <h3>Manual de Identidad de Marca</h3>
        <p>Guía completa de branding: paleta de colores, tipografías, logotipo y normas de uso.</p>
        <div class="tags"><span class="tag">PDF + Canva</span><span class="tag">22 páginas</span><span class="stars">★★★★☆ 4.6</span></div>
        <div class="card-foot">
          <div><span class="price-main">$79.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Manual Identidad de Marca','$79.000',79000,'🎨')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-purple"><span>📑</span><span class="badge badge-new">Nuevo</span></div>
      <div class="card-body">
        <h3>Kit de Presentaciones Premium</h3>
        <p>20 plantillas de PowerPoint con animaciones profesionales para ventas, inversores y equipos.</p>
        <div class="tags"><span class="tag">PPTX</span><span class="tag">Animaciones</span><span class="stars">★★★★★ 4.8</span></div>
        <div class="card-foot">
          <div><span class="price-old">$89.000</span><span class="price-main">$59.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Kit Presentaciones Premium','$59.000',59000,'📑')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-amber"><span>📬</span></div>
      <div class="card-body">
        <h3>Folleto de Ventas B2B Editable</h3>
        <p>Plantilla de folleto comercial para presentar servicios o productos a otras empresas. Diseño impactante.</p>
        <div class="tags"><span class="tag">Canva + PDF</span><span class="tag">A4 y A5</span><span class="stars">★★★★☆ 4.5</span></div>
        <div class="card-foot">
          <div><span class="price-main">$35.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Folleto de Ventas B2B','$35.000',35000,'📬')">+ Añadir</button>
        </div>
      </div>
    </div>
  </div>

  <!-- SERVICIOS -->
  <div class="panel grid" id="panel-servicios">
    <div class="card">
      <div class="card-vis cv-teal"><span>💡</span><span class="badge badge-corp">Corporativo</span></div>
      <div class="card-body">
        <h3>Consultoría Estratégica (sesión 2h)</h3>
        <p>Sesión personalizada con un experto para analizar tu modelo de negocio y definir el camino al crecimiento.</p>
        <div class="tags"><span class="tag">Online</span><span class="tag">Informe incluido</span><span class="stars">★★★★★ 5.0</span></div>
        <div class="card-foot">
          <div><span class="price-main">$250.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Consultoría Estratégica (2h)','$250.000',250000,'💡')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-blue"><span>🔍</span><span class="badge badge-corp">Corporativo</span></div>
      <div class="card-body">
        <h3>Auditoría de Presencia Digital</h3>
        <p>Evaluación completa de tu sitio web, redes sociales, posicionamiento SEO y reputación en línea.</p>
        <div class="tags"><span class="tag">Reporte PDF</span><span class="tag">Plan de acción</span><span class="stars">★★★★★ 4.9</span></div>
        <div class="card-foot">
          <div><span class="price-main">$320.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Auditoría Digital','$320.000',320000,'🔍')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-purple"><span>👥</span><span class="badge badge-corp">Corporativo</span></div>
      <div class="card-body">
        <h3>Capacitación Corporativa In-house</h3>
        <p>Taller presencial o virtual para tu equipo en Excel, Power BI, marketing digital o gestión de proyectos.</p>
        <div class="tags"><span class="tag">Hasta 20 personas</span><span class="tag">8 horas</span><span class="stars">★★★★★ 4.8</span></div>
        <div class="card-foot">
          <div><span class="price-main">$890.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Capacitación Corporativa','$890.000',890000,'👥')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-amber"><span>🗺️</span></div>
      <div class="card-body">
        <h3>Diseño de Procesos de Negocio (BPM)</h3>
        <p>Mapeo, documentación y optimización de los procesos clave de tu empresa para reducir costos y errores.</p>
        <div class="tags"><span class="tag">BPMN 2.0</span><span class="tag">Diagrama incluido</span><span class="stars">★★★★☆ 4.7</span></div>
        <div class="card-foot">
          <div><span class="price-main">$480.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Diseño de Procesos BPM','$480.000',480000,'🗺️')">+ Añadir</button>
        </div>
      </div>
    </div>
  </div>

  <!-- SOLUCIONES -->
  <div class="panel grid" id="panel-soluciones">
    <div class="card">
      <div class="card-vis cv-teal"><span>🏢</span><span class="badge badge-new">Nuevo</span></div>
      <div class="card-body">
        <h3>CRM para PYMES — Starter Pack</h3>
        <p>Gestión de clientes, pipeline de ventas, seguimiento de oportunidades y reportes automáticos.</p>
        <div class="tags"><span class="tag">Nube</span><span class="tag">Onboarding incluido</span><span class="stars">★★★★★ 4.9</span></div>
        <div class="card-foot">
          <div><span class="price-main">$190.000 <span class="price-cur">COP/mes</span></span></div>
          <button class="add-btn" onclick="addToCart('CRM PYMES Starter','$190.000/mes',190000,'🏢')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-blue"><span>⚡</span><span class="badge badge-hot">Popular</span></div>
      <div class="card-body">
        <h3>Automatización de Procesos (RPA)</h3>
        <p>Automatiza tareas repetitivas con bots inteligentes: facturación, reportes, correos y más.</p>
        <div class="tags"><span class="tag">Implementación</span><span class="tag">Soporte 30 días</span><span class="stars">★★★★★ 4.8</span></div>
        <div class="card-foot">
          <div><span class="price-main">$350.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Automatización RPA','$350.000',350000,'⚡')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-purple"><span>📂</span></div>
      <div class="card-body">
        <h3>Sistema de Gestión Documental</h3>
        <p>Digitaliza y organiza tus documentos corporativos con control de versiones, permisos y búsqueda inteligente.</p>
        <div class="tags"><span class="tag">Nube + Local</span><span class="tag">ISO 9001</span><span class="stars">★★★★☆ 4.6</span></div>
        <div class="card-foot">
          <div><span class="price-main">$280.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Sistema Gestión Documental','$280.000',280000,'📂')">+ Añadir</button>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-vis cv-amber"><span>📉</span><span class="badge badge-new">Nuevo</span></div>
      <div class="card-body">
        <h3>Dashboard de KPIs Empresariales</h3>
        <p>Panel de indicadores en tiempo real conectado a tus sistemas para decisiones gerenciales rápidas.</p>
        <div class="tags"><span class="tag">Power BI</span><span class="tag">Personalizable</span><span class="stars">★★★★★ 5.0</span></div>
        <div class="card-foot">
          <div><span class="price-main">$220.000 <span class="price-cur">COP</span></span></div>
          <button class="add-btn" onclick="addToCart('Dashboard KPIs','$220.000',220000,'📉')">+ Añadir</button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- BANNER OFERTA -->
<section class="banner" id="soluciones">
  <div class="banner-inner">
    <div>
      <div class="banner-ey">🔥 &nbsp; Oferta especial — Solo esta semana</div>
      <h2>Pack Todo en Uno para Empresas</h2>
      <p style="color:var(--t2);font-size:.875rem;max-width:380px;line-height:1.6">Obtén los 4 cursos más populares + el pack de plantillas corporativas + una sesión de consultoría estratégica. Todo en un solo paquete con descuento exclusivo.</p>
    </div>
    <div class="banner-price-wrap">
      <div class="banner-old" style="font-size:.82rem;color:var(--t3);text-decoration:line-through;margin-bottom:.25rem">$697.000 COP</div>
      <div class="banner-plabel" style="font-size:.75rem;color:var(--t2)">Precio del paquete</div>
      <div class="banner-price">$390.000</div>
      <div style="font-size:.75rem;color:var(--teal);margin:.2rem 0 .9rem;font-weight:600">Ahorra $307.000 COP</div>
      <button class="btn-cta" onclick="addToCart('Pack Todo en Uno Empresas','$390.000',390000,'🎁')">Quiero este paquete</button>
    </div>
  </div>
</section>

<!-- PAYMENT SECTION -->
<section class="paysec" id="pago">
  <div class="sec-head">
    <h2>Métodos de pago disponibles</h2>
    <p>Paga de forma segura con el método que prefieras. Procesamos tu compra al instante.</p>
  </div>
  <div class="trust">
    <div class="tbadge"><div class="ticon">🔒</div>Pago 100% seguro</div>
    <div class="tbadge"><div class="ticon">🛡️</div>SSL 256 bits</div>
    <div class="tbadge"><div class="ticon">✅</div>Factura electrónica</div>
    <div class="tbadge"><div class="ticon">↩️</div>Garantía 7 días</div>
  </div>
  <div class="pay-grid">
    <div class="pay-card">
      <div class="pay-icon pi-pse">PSE</div>
      <div class="pay-name">PSE</div>
      <div class="pay-desc">Débito bancario en línea</div>
    </div>
    <div class="pay-card">
      <div class="pay-icon pi-nequi">Nequi</div>
      <div class="pay-name">Nequi</div>
      <div class="pay-desc">Billetera digital Bancolombia</div>
    </div>
    <div class="pay-card">
      <div class="pay-icon pi-davi">Daviplata</div>
      <div class="pay-name">Daviplata</div>
      <div class="pay-desc">Billetera Davivienda</div>
    </div>
    <div class="pay-card">
      <div class="pay-icon pi-efecty">Efecty</div>
      <div class="pay-name">Efecty</div>
      <div class="pay-desc">Pago en efectivo</div>
    </div>
    <div class="pay-card">
      <div class="pay-icon pi-visa">VISA</div>
      <div class="pay-name">Visa</div>
      <div class="pay-desc">Crédito o débito</div>
    </div>
    <div class="pay-card">
      <div class="pay-icon pi-mc">MC</div>
      <div class="pay-name">Mastercard</div>
      <div class="pay-desc">Crédito o débito</div>
    </div>
    <div class="pay-card">
      <div class="pay-icon pi-pp">PayPal</div>
      <div class="pay-name">PayPal</div>
      <div class="pay-desc">Pago internacional</div>
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="foot-inner">
    <div class="foot-logo">Pro<span>Academy</span></div>
    <ul class="foot-links">
      <li><a href="#">Términos y condiciones</a></li>
      <li><a href="#">Política de privacidad</a></li>
      <li><a href="#">Soporte</a></li>
      <li><a href="#">Contacto</a></li>
    </ul>
    <div class="foot-copy">© 2025 ProAcademy. Todos los derechos reservados.</div>
  </div>
</footer>

<!-- MODAL / CHECKOUT -->
<div class="overlay" id="overlay" onclick="handleOverlayClick(event)">
  <div class="modal" id="modal">
    <!-- STEP 0: CARRITO -->
    <div class="step on" id="step0">
      <div class="modal-h">
        <h3>🛒 Tu carrito</h3>
        <button class="close-btn" onclick="closeCart()">✕</button>
      </div>
      <div class="modal-b" id="cartItems">
        <div class="empty-cart">Tu carrito está vacío.<br>¡Agrega algo para comenzar!</div>
      </div>
      <div class="modal-f" id="cartFooter" style="display:none">
        <button class="btn-back" onclick="closeCart()">Seguir comprando</button>
        <button class="btn-go" onclick="goTo(1)">Pagar →</button>
      </div>
    </div>

    <!-- STEP 1: DATOS -->
    <div class="step" id="step1">
      <div class="modal-h">
        <h3>Datos personales</h3>
        <button class="close-btn" onclick="closeCart()">✕</button>
      </div>
      <div class="modal-b">
        <div class="step-title">Paso 1 de 3 — ¿A quién le enviamos la factura?</div>
        <div class="frow half">
          <div>
            <label>Nombre</label>
            <input type="text" id="nombre" placeholder="Juan">
          </div>
          <div>
            <label>Apellido</label>
            <input type="text" id="apellido" placeholder="Pérez">
          </div>
        </div>
        <div class="frow">
          <label>Correo electrónico</label>
          <input type="email" id="email" placeholder="juan@empresa.com">
        </div>
        <div class="frow">
          <label>Empresa (opcional)</label>
          <input type="text" id="empresa" placeholder="Mi Empresa S.A.S.">
        </div>
        <div class="frow">
          <label>NIT / Cédula</label>
          <input type="text" id="nit" placeholder="900.123.456-7">
        </div>
      </div>
      <div class="modal-f">
        <button class="btn-back" onclick="goTo(0)">← Volver</button>
        <button class="btn-go" onclick="goTo(2)">Continuar →</button>
      </div>
    </div>

    <!-- STEP 2: PAGO -->
    <div class="step" id="step2">
      <div class="modal-h">
        <h3>Método de pago</h3>
        <button class="close-btn" onclick="closeCart()">✕</button>
      </div>
      <div class="modal-b">
        <div class="step-title">Paso 2 de 3 — Elige cómo pagar</div>
        <div class="pm-pick">
          <div class="pm-opt sel" onclick="selectPM(this,'tarjeta')"><div class="pm-ring"></div>💳 Tarjeta</div>
          <div class="pm-opt" onclick="selectPM(this,'pse')"><div class="pm-ring"></div>🏦 PSE</div>
          <div class="pm-opt" onclick="selectPM(this,'nequi')"><div class="pm-ring"></div>📱 Nequi</div>
          <div class="pm-opt" onclick="selectPM(this,'daviplata')"><div class="pm-ring"></div>📱 Daviplata</div>
          <div class="pm-opt" onclick="selectPM(this,'efecty')"><div class="pm-ring"></div>💵 Efecty</div>
          <div class="pm-opt" onclick="selectPM(this,'paypal')"><div class="pm-ring"></div>🌐 PayPal</div>
        </div>

        <!-- Tarjeta -->
        <div class="cc-fields show" id="cc-tarjeta">
          <div class="frow">
            <label>Número de tarjeta</label>
            <input type="text" id="ccnum" placeholder="•••• •••• •••• ••••" maxlength="19" oninput="fmtCC(this)">
          </div>
          <div class="frow half">
            <div>
              <label>Vencimiento</label>
              <input type="text" id="ccexp" placeholder="MM/AA" maxlength="5" oninput="fmtExp(this)">
            </div>
            <div>
              <label>CVV</label>
              <input type="text" id="cccvv" placeholder="•••" maxlength="3">
            </div>
          </div>
          <div class="frow">
            <label>Nombre en la tarjeta</label>
            <input type="text" id="ccname" placeholder="JUAN PÉREZ">
          </div>
        </div>

        <!-- PSE -->
        <div class="cc-fields" id="cc-pse">
          <div class="frow">
            <label>Banco</label>
            <select>
              <option>Bancolombia</option>
              <option>Davivienda</option>
              <option>Banco de Bogotá</option>
              <option>BBVA Colombia</option>
              <option>Banco Popular</option>
              <option>Colpatria</option>
            </select>
          </div>
          <div class="frow">
            <label>Tipo de cuenta</label>
            <select><option>Cuenta de ahorros</option><option>Cuenta corriente</option></select>
          </div>
        </div>

        <!-- Nequi / Daviplata -->
        <div class="cc-fields" id="cc-nequi">
          <div class="frow">
            <label>Número de celular Nequi</label>
            <input type="tel" placeholder="300 000 0000">
          </div>
          <p style="font-size:.75rem;color:var(--t2);margin-top:.5rem">Recibirás una notificación push para aprobar el pago.</p>
        </div>
        <div class="cc-fields" id="cc-daviplata">
          <div class="frow">
            <label>Número de celular Daviplata</label>
            <input type="tel" placeholder="300 000 0000">
          </div>
          <p style="font-size:.75rem;color:var(--t2);margin-top:.5rem">Te enviaremos un código de confirmación por SMS.</p>
        </div>

        <!-- Efecty -->
        <div class="cc-fields" id="cc-efecty">
          <p style="font-size:.85rem;color:var(--t2);line-height:1.6">Al confirmar, recibirás un código de pago en tu correo. Preséntalo en cualquier punto Efecty del país. Tu acceso se activa al confirmar el pago.</p>
        </div>

        <!-- PayPal -->
        <div class="cc-fields" id="cc-paypal">
          <p style="font-size:.85rem;color:var(--t2);line-height:1.6">Serás redirigido a PayPal para completar tu pago de forma segura en dólares estadounidenses.</p>
        </div>

        <!-- Resumen -->
        <div style="background:var(--s2);border:1px solid var(--border);border-radius:10px;padding:1rem;margin-top:1rem">
          <div style="display:flex;justify-content:space-between;font-size:.8rem;color:var(--t2);margin-bottom:.4rem">
            <span>Subtotal</span><span id="subtotalLabel">$0</span>
          </div>
          <div style="display:flex;justify-content:space-between;font-size:.8rem;color:var(--t2);margin-bottom:.4rem">
            <span>IVA (19%)</span><span id="ivaLabel">$0</span>
          </div>
          <div style="display:flex;justify-content:space-between;font-size:.95rem;font-weight:600;padding-top:.5rem;border-top:1px solid var(--border)">
            <span>Total</span><span id="totalLabel" style="color:var(--teal)">$0</span>
          </div>
        </div>
      </div>
      <div class="modal-f">
        <button class="btn-back" onclick="goTo(1)">← Volver</button>
        <button class="btn-go" onclick="processPay()">Confirmar pago 🔒</button>
      </div>
    </div>

    <!-- STEP 3: ÉXITO -->
    <div class="step" id="step3">
      <div class="modal-h">
        <h3>¡Compra confirmada!</h3>
        <button class="close-btn" onclick="closeCart()">✕</button>
      </div>
      <div class="modal-b">
        <div class="success-wrap">
          <div class="suc-ico">✅</div>
          <h3>¡Pago procesado con éxito!</h3>
          <p>Hemos enviado el acceso a tus productos al correo registrado.<br><br>En los próximos minutos recibirás tus materiales y la factura electrónica.</p>
          <div style="margin-top:1.5rem;background:var(--s2);border:1px solid var(--border);border-radius:10px;padding:1rem;text-align:left">
            <div style="font-size:.75rem;color:var(--t2);margin-bottom:.4rem">Código de orden</div>
            <div style="font-size:.95rem;font-weight:600;color:var(--teal)" id="orderCode">#PA-2025-0001</div>
          </div>
        </div>
      </div>
      <div class="modal-f">
        <button class="btn-go" onclick="closeAndReset()" style="flex:1">Cerrar</button>
      </div>
    </div>
  </div>
</div>

<!-- TOAST -->
<div class="toast" id="toast">
  <div class="toast-dot"></div>
  <span id="toastMsg">Producto añadido</span>
</div>

<script>
let cart=[];
let selPM='tarjeta';

function showTab(name,btn){
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
  document.getElementById('panel-'+name).classList.add('active');
  btn.classList.add('active');
}

function addToCart(name,price,amount,emoji){
  const existing=cart.find(i=>i.name===name);
  if(existing){existing.qty++;}
  else{cart.push({name,price,amount,emoji,qty:1});}
  updateCartCount();
  showToast('✓ "'+name+'" añadido al carrito');
}

function updateCartCount(){
  const total=cart.reduce((s,i)=>s+i.qty,0);
  const el=document.getElementById('cartCount');
  el.textContent=total;
  el.classList.remove('bump');
  void el.offsetWidth;
  el.classList.add('bump');
  setTimeout(()=>el.classList.remove('bump'),350);
}

function openCart(){
  renderCart();
  document.getElementById('overlay').classList.add('open');
  goTo(0);
}

function closeCart(){document.getElementById('overlay').classList.remove('open')}

function handleOverlayClick(e){if(e.target===document.getElementById('overlay'))closeCart();}

function renderCart(){
  const el=document.getElementById('cartItems');
  const ftr=document.getElementById('cartFooter');
  if(!cart.length){
    el.innerHTML='<div class="empty-cart">Tu carrito está vacío.<br>¡Agrega algo para comenzar!</div>';
    ftr.style.display='none';
    return;
  }
  let html='';
  cart.forEach((item,idx)=>{
    html+=`<div class="ci">
      <div class="ci-emo">${item.emoji}</div>
      <div class="ci-info"><h4>${item.name}</h4><p>${item.price}${item.qty>1?' × '+item.qty:''}</p></div>
      <div class="ci-price">${fmtCOP(item.amount*item.qty)}</div>
      <button class="rm-btn" onclick="removeItem(${idx})">✕</button>
    </div>`;
  });
  const sub=cart.reduce((s,i)=>s+i.amount*i.qty,0);
  html+=`<div class="cart-total-row"><span class="ct-label">Total</span><span class="ct-amount">${fmtCOP(sub)}</span></div>`;
  el.innerHTML=html;
  ftr.style.display='flex';
}

function removeItem(idx){
  cart.splice(idx,1);
  updateCartCount();
  renderCart();
}

function goTo(n){
  document.querySelectorAll('.step').forEach(s=>s.classList.remove('on'));
  document.getElementById('step'+n).classList.add('on');
  if(n===2)updateSummary();
}

function updateSummary(){
  const sub=cart.reduce((s,i)=>s+i.amount*i.qty,0);
  const iva=Math.round(sub*0.19);
  const total=sub+iva;
  document.getElementById('subtotalLabel').textContent=fmtCOP(sub);
  document.getElementById('ivaLabel').textContent=fmtCOP(iva);
  document.getElementById('totalLabel').textContent=fmtCOP(total);
}

function selectPM(el,pm){
  document.querySelectorAll('.pm-opt').forEach(o=>o.classList.remove('sel'));
  document.querySelectorAll('.cc-fields').forEach(f=>f.classList.remove('show'));
  el.classList.add('sel');
  selPM=pm;
  const f=document.getElementById('cc-'+pm);
  if(f)f.classList.add('show');
}

function processPay(){
  const code='#PA-2025-'+String(Math.floor(Math.random()*9000)+1000);
  document.getElementById('orderCode').textContent=code;
  goTo(3);
}

function closeAndReset(){
  cart=[];
  updateCartCount();
  closeCart();
}

function fmtCOP(n){
  return '$'+n.toLocaleString('es-CO');}

function fmtCC(inp){
  let v=inp.value.replace(/\D/g,'').substring(0,16);
  inp.value=v.replace(/(.{4})/g,'$1 ').trim();
}

function fmtExp(inp){
  let v=inp.value.replace(/\D/g,'').substring(0,4);
  if(v.length>2)v=v.substring(0,2)+'/'+v.substring(2);
  inp.value=v;
}

function showToast(msg){
  const t=document.getElementById('toast');
  document.getElementById('toastMsg').textContent=msg;
  t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),2500);
}

function searchProducts(){
  const q=document.getElementById('searchInput').value.toLowerCase().trim();
  if(!q)return;
  const panels=['cursos','folletos','servicios','soluciones'];
  for(const p of panels){
    const el=document.getElementById('panel-'+p);
    const cards=el.querySelectorAll('.card');
    let found=false;
    cards.forEach(c=>{
      const txt=c.textContent.toLowerCase();
      if(txt.includes(q)){found=true;}
    });
    if(found){
      document.querySelectorAll('.panel').forEach(x=>x.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
      el.classList.add('active');
      const btn=[...document.querySelectorAll('.tab-btn')].find(b=>b.getAttribute('onclick')&&b.getAttribute('onclick').includes("'"+p+"'"));
      if(btn)btn.classList.add('active');
      el.scrollIntoView({behavior:'smooth',block:'start'});
      return;
    }
  }
  showToast('No se encontraron resultados para "'+q+'"');
}
</script>
</body>
</html>
