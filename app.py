import streamlit as st

st.set_page_config(
    page_title="Laura Martínez Alzate | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:#050e09!important;color:#e2f0e8!important;font-family:'Outfit',sans-serif}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],footer,#MainMenu{display:none!important}
.block-container{padding:0!important;max-width:100%!important}
.pg{min-height:100vh;padding:32px 4vw 64px;background:radial-gradient(ellipse 60% 45% at 0% 0%,rgba(0,255,140,.055) 0%,transparent 60%),radial-gradient(ellipse 40% 30% at 100% 100%,rgba(0,200,110,.04) 0%,transparent 55%),#050e09}
.nav{display:flex;align-items:center;justify-content:space-between;padding-bottom:28px;margin-bottom:28px;border-bottom:1px solid rgba(0,255,140,.08)}
.nav-logo{font-family:'Syne',sans-serif;font-weight:800;font-size:1rem;color:#e2f0e8;letter-spacing:-.02em}
.nav-logo b{color:#00ff8c}
.nav-links{display:flex;gap:24px}
.nav-link{font-family:'JetBrains Mono',monospace;font-size:.63rem;color:rgba(226,240,232,.3);letter-spacing:.12em;text-transform:uppercase}
.nav-pill{display:flex;align-items:center;gap:7px;border:1px solid rgba(0,255,140,.22);border-radius:100px;padding:5px 14px;font-family:'JetBrains Mono',monospace;font-size:.62rem;color:#00ff8c;letter-spacing:.1em;background:rgba(0,255,140,.06)}
.nav-pill::before{content:'';width:6px;height:6px;border-radius:50%;background:#00ff8c;box-shadow:0 0 7px #00ff8c;animation:dot 2.2s ease-in-out infinite}
@keyframes dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.3;transform:scale(.75)}}
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:12px}
.c{border-radius:18px;border:1px solid rgba(0,255,140,.08);background:rgba(255,255,255,.022);padding:28px;position:relative;overflow:hidden;transition:border-color .25s,transform .22s,box-shadow .25s}
.c::before{content:'';position:absolute;inset:0;border-radius:18px;background:linear-gradient(135deg,rgba(0,255,140,.04) 0%,transparent 50%);opacity:0;transition:opacity .25s;pointer-events:none}
.c:hover{border-color:rgba(0,255,140,.26);transform:translateY(-3px);box-shadow:0 18px 50px rgba(0,0,0,.5),0 0 22px rgba(0,255,140,.06)}
.c:hover::before{opacity:1}
.hero-c{grid-column:span 7;background:rgba(0,255,140,.025);border-color:rgba(0,255,140,.12);padding:44px 46px}
.hero-eyebrow{font-family:'JetBrains Mono',monospace;font-size:.63rem;color:#00ff8c;letter-spacing:.16em;text-transform:uppercase;margin-bottom:20px;opacity:.75}
.hero-name{font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(2rem,4.2vw,3.8rem);line-height:1.0;letter-spacing:-.035em;color:#e2f0e8}
.hero-name span{color:#00ff8c;text-shadow:0 0 32px rgba(0,255,140,.28)}
.hero-role{font-family:'JetBrains Mono',monospace;font-size:.75rem;color:rgba(226,240,232,.35);margin-top:16px;letter-spacing:.04em}
.hero-desc{font-size:.92rem;font-weight:300;color:rgba(226,240,232,.54);line-height:1.8;max-width:440px;margin-top:20px}
.hero-cta{display:inline-flex;align-items:center;gap:10px;margin-top:30px;padding:11px 24px;border-radius:100px;border:1px solid rgba(0,255,140,.3);background:rgba(0,255,140,.08);font-family:'JetBrains Mono',monospace;font-size:.7rem;color:#00ff8c;letter-spacing:.1em;text-decoration:none;transition:background .2s,border-color .2s}
.stat-col{grid-column:span 2;display:flex;flex-direction:column;gap:12px}
.stat-box{flex:1;border-radius:16px;border:1px solid rgba(0,255,140,.08);background:rgba(255,255,255,.022);padding:18px 20px;display:flex;flex-direction:column;justify-content:space-between;transition:border-color .22s}
.stat-box:hover{border-color:rgba(0,255,140,.28)}
.stat-n{font-family:'Syne',sans-serif;font-weight:800;font-size:2.4rem;color:#00ff8c;line-height:1}
.stat-l{font-size:.66rem;font-weight:500;color:rgba(226,240,232,.33);letter-spacing:.08em;text-transform:uppercase;margin-top:8px}
.skills-c{grid-column:span 3}
.about-c{grid-column:span 3}
.c-lbl{font-family:'JetBrains Mono',monospace;font-size:.58rem;color:rgba(0,255,140,.48);letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px}
.c-ttl{font-family:'Syne',sans-serif;font-weight:700;font-size:.96rem;color:#e2f0e8;margin-bottom:14px}
.tags{display:flex;flex-wrap:wrap;gap:7px}
.tag{background:rgba(0,255,140,.07);border:1px solid rgba(0,255,140,.13);border-radius:7px;padding:4px 11px;font-family:'JetBrains Mono',monospace;font-size:.64rem;color:rgba(0,255,140,.78)}
.about-txt{font-size:.81rem;font-weight:300;color:rgba(226,240,232,.44);line-height:1.8;margin-top:6px}
.about-loc{margin-top:16px;display:flex;align-items:center;gap:8px;font-family:'JetBrains Mono',monospace;font-size:.63rem;color:rgba(0,255,140,.48)}
.about-loc::before{content:'◎';font-size:.7rem}
.sec-row{grid-column:span 12;background:transparent!important;border:1px solid transparent!important;padding:16px 0 4px;display:flex;align-items:center;gap:16px}
.sec-row:hover{transform:none!important;box-shadow:none!important}
.sec-row::before{display:none!important}
.sec-n{font-family:'JetBrains Mono',monospace;font-size:.58rem;color:rgba(0,255,140,.32);letter-spacing:.12em;flex-shrink:0}
.sec-t{font-family:'Syne',sans-serif;font-weight:800;font-size:clamp(1.1rem,2vw,1.55rem);color:#e2f0e8;letter-spacing:-.025em;flex-shrink:0}
.sec-line{flex:1;height:1px;background:linear-gradient(90deg,rgba(0,255,140,.2) 0%,transparent 70%)}
.sec-count{font-family:'JetBrains Mono',monospace;font-size:.58rem;color:rgba(0,255,140,.32);flex-shrink:0}
.proj-c{grid-column:span 3;text-decoration:none!important;display:block;cursor:pointer;color:inherit!important}
.proj-head{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:14px}
.proj-ico{width:40px;height:40px;border-radius:11px;flex-shrink:0;background:rgba(0,255,140,.08);border:1px solid rgba(0,255,140,.15);display:flex;align-items:center;justify-content:center;font-size:1.1rem}
.proj-idx{font-family:'JetBrains Mono',monospace;font-size:.56rem;color:rgba(0,255,140,.26);letter-spacing:.1em}
.proj-ttl{font-family:'Syne',sans-serif;font-weight:700;font-size:.88rem;color:#e2f0e8;line-height:1.3;margin-bottom:7px}
.proj-dsc{font-size:.74rem;font-weight:300;color:rgba(226,240,232,.37);line-height:1.65;margin-bottom:16px}
.proj-foot{display:flex;align-items:center;justify-content:space-between;gap:8px}
.proj-tags{display:flex;gap:5px;flex-wrap:wrap}
.proj-tag{background:rgba(0,255,140,.055);border:1px solid rgba(0,255,140,.11);border-radius:5px;padding:2px 7px;font-family:'JetBrains Mono',monospace;font-size:.56rem;color:rgba(0,255,140,.58)}
.arr{width:26px;height:26px;border-radius:7px;flex-shrink:0;background:rgba(0,255,140,.07);border:1px solid rgba(0,255,140,.15);display:flex;align-items:center;justify-content:center;font-size:.72rem;color:#00ff8c;transition:all .22s}
.proj-c:hover .arr{background:rgba(0,255,140,.18);border-color:rgba(0,255,140,.5);transform:translate(2px,-2px)}
.quote-c{grid-column:span 6;background:rgba(0,255,140,.028);border-color:rgba(0,255,140,.11);padding:36px 40px;display:flex;flex-direction:column;justify-content:center}
.q-mark{font-family:'Syne',sans-serif;font-size:3.5rem;color:rgba(0,255,140,.17);line-height:1;margin-bottom:8px}
.q-txt{font-size:.98rem;font-weight:300;font-style:italic;color:rgba(226,240,232,.54);line-height:1.78}
.q-author{margin-top:16px;font-family:'JetBrains Mono',monospace;font-size:.63rem;color:rgba(0,255,140,.42);letter-spacing:.1em}
.contact-c{grid-column:span 6}
.contact-items{display:flex;flex-direction:column;gap:10px;margin-top:12px}
.contact-item{display:flex;align-items:center;gap:12px;padding:12px 16px;border-radius:11px;background:rgba(255,255,255,.018);border:1px solid rgba(0,255,140,.07)}
.c-ico{font-size:.95rem;flex-shrink:0}
.c-lbl2{font-size:.68rem;color:rgba(226,240,232,.32);margin-bottom:2px}
.c-val{font-family:'JetBrains Mono',monospace;font-size:.65rem;color:rgba(0,255,140,.58)}
.footer{margin-top:40px;padding-top:22px;border-top:1px solid rgba(0,255,140,.07);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px}
.footer-l{font-family:'Syne',sans-serif;font-weight:700;font-size:.86rem;color:#e2f0e8}
.footer-r{font-family:'JetBrains Mono',monospace;font-size:.58rem;color:rgba(226,240,232,.18)}
::-webkit-scrollbar{width:5px}
::-webkit-scrollbar-track{background:#050e09}
::-webkit-scrollbar-thumb{background:rgba(0,255,140,.17);border-radius:3px}
</style>
""", unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
projects = [
    {"t": "App de Audio",     "d": "Procesamiento y análisis de audio con interfaces interactivas.",      "i": "🎵", "url": "https://app-audio.streamlit.app/",                                  "tags": ["Audio", "DSP"]},
    {"t": "Detección CV",     "d": "Detección inteligente con visión por computadora y modelos ML.",      "i": "🔍", "url": "https://detecci-n-68fgkrrhas8ydz2moh8zbu.streamlit.app/",         "tags": ["CV", "ML"]},
    {"t": "Web Intro",        "d": "Página de introducción y presentación personal interactiva.",         "i": "🌐", "url": "https://miwebintro.streamlit.app/",                              "tags": ["Web", "UI"]},
    {"t": "Sentimientos NLP", "d": "Clasificación emocional de textos con NLP en tiempo real.",          "i": "🧠", "url": "https://sentimentoslaura.streamlit.app/",                       "tags": ["NLP", "AI"]},
    {"t": "TDF Español",      "d": "Procesamiento y análisis lingüístico de texto en español.",          "i": "📝", "url": "https://tdfesp-dmqheyywqfh4bqbcyvgtnx.streamlit.app/",          "tags": ["NLP", "Texto"]},
    {"t": "Proyecto HN",      "d": "Análisis avanzado y visualización de datos estructurados.",          "i": "📊", "url": "https://hnlatmk6qyahgosdlysqu2.streamlit.app/",                 "tags": ["Data", "Viz"]},
    {"t": "Word Cloud",       "d": "Generador visual de nubes de palabras personalizadas.",              "i": "☁️", "url": "https://wordcloudlaura.streamlit.app/",                        "tags": ["Viz", "NLP"]},
    {"t": "OCR",              "d": "Reconocimiento óptico de caracteres y extracción de texto.",         "i": "👁️", "url": "https://ocrlauramartinez.streamlit.app/",                      "tags": ["OCR", "CV"]},
    {"t": "OCR + Audio",      "d": "OCR combinado con síntesis de voz para leer documentos.",            "i": "🔊", "url": "https://ocr-audio-lauramartinez.streamlit.app/",                "tags": ["OCR", "Audio"]},
    {"t": "MQTT Receptor",    "d": "Recepción y monitoreo de mensajes mediante protocolo MQTT.",         "i": "📡", "url": "https://recepmqtt-lauramartinez.streamlit.app/",                "tags": ["IoT", "MQTT"]},
    {"t": "MQTT Emisor",      "d": "Publicación de mensajes en broker MQTT en tiempo real.",             "i": "📤", "url": "https://sendcmqtt-lauramaertinez.streamlit.app/",               "tags": ["IoT", "MQTT"]},
    {"t": "Chat PDF",         "d": "Conversa con documentos PDF usando inteligencia artificial.",        "i": "💬", "url": "https://chatpdf-wuh2rzvhoofnbptnvewxrz.streamlit.app/",         "tags": ["AI", "LLM"]},
    {"t": "Control por Voz",  "d": "Control de apps mediante comandos de voz en tiempo real.",           "i": "🎤", "url": "https://ctrlvoice-lauramartinez.streamlit.app/",                "tags": ["Voz", "CV"]},
    {"t": "Draw App",         "d": "Aplicación de dibujo y creación visual interactiva.",                "i": "✏️", "url": "https://drawlauramartinez.streamlit.app/",                     "tags": ["CV", "UI"]},
    {"t": "Hand Draw",        "d": "Dibujo mediante detección de gestos con las manos.",                 "i": "🖐️", "url": "https://drawhandlauramartinez.streamlit.app/",                 "tags": ["Gestos", "CV"]},
    {"t": "Vision App",       "d": "Visión artificial para análisis y reconocimiento visual avanzado.",  "i": "🤖", "url": "https://visionapp-lauramartinez.streamlit.app/",                "tags": ["AI", "CV"]},
]

# ── Render page sections individually (avoids giant f-string issues) ──────────

st.markdown("""
<div class="pg">
<nav class="nav">
  <div class="nav-logo">Laura<b>.</b>dev</div>
  <div class="nav-links">
    <span class="nav-link">Proyectos</span>
    <span class="nav-link">Skills</span>
    <span class="nav-link">Contacto</span>
  </div>
  <div class="nav-pill">Disponible para proyectos</div>
</nav>
<div class="grid">

  <div class="c hero-c">
    <div class="hero-eyebrow">// Data Science &middot; ML &middot; Computer Vision &middot; 2025</div>
    <div class="hero-name">Laura<br><span>Mart&#237;nez</span><br>Alzate</div>
    <div class="hero-role">Data Scientist &amp; Machine Learning Engineer</div>
    <div class="hero-desc">Transformo datos en soluciones inteligentes. Especializada en visi&#243;n por computadora, NLP, IoT y aplicaciones de IA desplegadas en producci&#243;n.</div>
    <a class="hero-cta" href="#">Ver proyectos &#8594;</a>
  </div>

  <div class="stat-col">
    <div class="stat-box"><div class="stat-n">16</div><div class="stat-l">Apps en producci&#243;n</div></div>
    <div class="stat-box"><div class="stat-n">8+</div><div class="stat-l">Tecnolog&#237;as</div></div>
    <div class="stat-box"><div class="stat-n">AI</div><div class="stat-l">Especialidad core</div></div>
  </div>

  <div class="c skills-c">
    <div class="c-lbl">// Stack tecnol&#243;gico</div>
    <div class="c-ttl">Habilidades</div>
    <div class="tags">
      <span class="tag">Python</span><span class="tag">Streamlit</span>
      <span class="tag">OpenCV</span><span class="tag">TensorFlow</span>
      <span class="tag">NLP</span><span class="tag">MQTT</span>
      <span class="tag">OCR</span><span class="tag">LLMs</span>
      <span class="tag">Data Viz</span><span class="tag">Audio DSP</span>
      <span class="tag">GitHub</span><span class="tag">Scikit-learn</span>
    </div>
  </div>

  <div class="c about-c">
    <div class="c-lbl">// Sobre m&#237;</div>
    <div class="c-ttl">Perfil</div>
    <div class="about-txt">Apasionada por convertir datos en experiencias &#250;tiles e impactantes. Trabajo con visi&#243;n por computadora, NLP, IoT y despliegue de apps de inteligencia artificial en la nube.</div>
    <div class="about-loc">Medell&#237;n, Colombia</div>
  </div>

  <div class="c sec-row">
    <span class="sec-n">01</span>
    <span class="sec-t">Proyectos</span>
    <span class="sec-line"></span>
    <span class="sec-count">16 aplicaciones desplegadas</span>
  </div>
""", unsafe_allow_html=True)

# ── Project cards ─────────────────────────────────────────────────────────────
for i, p in enumerate(projects):
    idx = str(i + 1).zfill(2)
    tags_html = "".join(f'<span class="proj-tag">{t}</span>' for t in p["tags"])
    st.markdown(f"""
<a href="{p['url']}" target="_blank" class="c proj-c">
  <div class="proj-head">
    <div class="proj-ico">{p['i']}</div>
    <span class="proj-idx">PRJ_{idx}</span>
  </div>
  <div class="proj-ttl">{p['t']}</div>
  <div class="proj-dsc">{p['d']}</div>
  <div class="proj-foot">
    <div class="proj-tags">{tags_html}</div>
    <div class="arr">&#8599;</div>
  </div>
</a>""", unsafe_allow_html=True)

# ── Bottom sections ────────────────────────────────────────────────────────────
st.markdown("""
  <div class="c sec-row">
    <span class="sec-n">02</span>
    <span class="sec-t">M&#225;s sobre m&#237;</span>
    <span class="sec-line"></span>
  </div>

  <div class="c quote-c">
    <div class="q-mark">&#8220;</div>
    <div class="q-txt">Los datos son el nuevo lenguaje universal. Mi misi&#243;n es traducirlos en herramientas que la gente pueda ver, sentir y usar en su d&#237;a a d&#237;a.</div>
    <div class="q-author">&#8212; Laura Mart&#237;nez Alzate</div>
  </div>

  <div class="c contact-c">
    <div class="c-lbl">// Contacto</div>
    <div class="c-ttl">Hablemos</div>
    <div class="contact-items">
      <div class="contact-item">
        <span class="c-ico">&#128231;</span>
        <div><div class="c-lbl2">Email</div><div class="c-val">lauramartinezalzate5550@gmail.com</div></div>
      </div>
      <div class="contact-item">
        <span class="c-ico">&#128025;</span>
        <div><div class="c-lbl2">GitHub</div><div class="c-val">github.com/fhasivia</div></div>
      </div>
      <div class="contact-item">
        <span class="c-ico">&#128205;</span>
        <div><div class="c-lbl2">Ubicaci&#243;n</div><div class="c-val">Medell&#237;n, Antioquia, Colombia</div></div>
      </div>
    </div>
  </div>

</div>

<div class="footer">
  <div class="footer-l">Laura Mart&#237;nez Alzate &middot; Portfolio 2025</div>
  <div class="footer-r">Built with Python &amp; Streamlit &middot; Medell&#237;n &#127464;&#127476;</div>
</div>

</div>
""", unsafe_allow_html=True)
