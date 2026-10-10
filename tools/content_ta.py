"""Tamil text for qos.ae. Same structure as content_en.py."""

FIG = '<img class="{cls}" src="@R@assets/img/{name}.svg" alt="{alt}" width="{w}" height="{h}" loading="lazy"><p class="caption">விளக்கப்படம்</p>'


def fig(name, alt, tablet=False):
    w, h, cls = (960, 640, "tablet") if tablet else (360, 720, "phone")
    return '<div>' + FIG.format(cls=cls, name=name, alt=alt, w=w, h=h) + '</div>'


BEYOND = [
    ("apps", "கைபேசிச் செயலிகள்",
     "முனையத்திலிருந்தே ஆண்ட்ராய்டு செயலிகளைக் கட்டலாம்: Java 21, Kotlin, Gradle, aapt2, d8, apksigner, adb அனைத்தும் தொகுப்புத் திரட்டில் உள்ளன. வலைச் செயலிகள் முழுமையாக இயங்கும்.",
     "ஒரே படியில் அமையும் ஆண்ட்ராய்டு கருவித்தொகுப்பு; ஒரே கட்டளையில் அதே கைபேசியில் கட்டி நிறுவும் தொடக்கத் திட்டம்.",
     "மடிக்கணினியை விடக் கட்டுமானம் மெதுவாக நடக்கும். Flutter இன்னும் ஆண்ட்ராய்டு சாதனங்களில் இயங்காது."),
    ("games", "விளையாட்டுகள்",
     "HTML5, JavaScript-இல் வலை விளையாட்டுகள்; எந்த மொழியிலும் உரை விளையாட்டுகள். qos Desktop உடன்: Godot 4, LÖVE, pygame, raylib.",
     "தொடக்கத் திட்டங்களுடன் ஒரே படியில் அமையும் விளையாட்டுக் கருவித்தொகுப்பு.",
     "2D-யும் எளிய 3D-யும் மட்டும். கனமான 3D விளையாட்டுகளுக்குத் தேவையான வரைகலை இயக்கிகள் கைபேசிகளில் இல்லை."),
    ("animation", "கார்ட்டூன்களும் அசைவூட்டமும்",
     "manim கொண்டு விளக்க அசைவூட்டங்கள், ImageMagick கொண்டு படப் பணிகள். qos Desktop உடன்: Krita-வில் சட்டகம் சட்டகமாக அசைவூட்டம், Inkscape, GIMP-இல் வரைதல்.",
     "இந்தக் கருவிகள் ஒரே படியில் அமையும் படைப்புக் கருவித்தொகுப்பு.",
     "Blender இல்லை, எனவே 3D அசைவூட்டம் இல்லை. நீண்ட வரைவாக்கங்கள் மெதுவாக நடக்கும், கைபேசி சூடாகும்."),
    ("film", "திரைப்படங்கள்",
     "ffmpeg கொண்டு தொகுக்கலாம்: வெட்டுதல், இணைத்தல், இசை, தமிழ் வசனவரிகள் சேர்த்தல், YouTube அல்லது WhatsApp-க்கு ஏற்றுமதி. qos Desktop உடன்: Kdenlive, Shotcut, Audacity.",
     "தொகுப்பு, ஒலி, வசனவரிக் கருவிகள் ஒரே படியில் அமையும் திரைப்படக் கருவித்தொகுப்பு.",
     "படம்பிடிப்பது கைபேசியின் சொந்தக் கேமரா செயலியில்; qos காட்சிகளைத் தொகுக்கும். 4K காணொளி வரைவாக்கம் மெதுவாக இருக்கும்."),
    ("iot", "IoT",
     "Mosquitto கொண்டு MQTT, Python, Node.js சேவைகள், Wi-Fi வழியே ESP32 அல்லது Arduino பலகைகளுடன் தொடர்பு.",
     "IoT கருவித்தொகுப்பு: MQTT தரகர், கட்டுப்பாட்டுப் பலகைகள், ESP32 பலகைகளுக்கு வான்வழிப் புதுப்பிப்புகள்.",
     "ரூட் இல்லாமல் USB வழியே பலகைகளில் நிரலேற்றுவது ஆண்ட்ராய்டில் கடினம். அதையும், கைபேசியிலிருந்தே Arduino-வில் இ-தமிழையும் ஆராய்ந்து வருகிறோம்."),
    ("security", "இணையப் பாதுகாப்பு",
     "nmap கொண்டு உங்கள் சொந்த வலையமைப்பை வருடலாம்; GnuPG, age கொண்டு மறையாக்கம்; WireGuard, Tor; ClamAV, YARA கொண்டு கோப்புச் சோதனை; radare2, gdb, apktool, jadx கொண்டு நிரல்களையும் ஆண்ட்ராய்டு செயலிகளையும் பிரித்தாய்தல்.",
     "கற்பதற்கும் காப்பதற்குமான பாதுகாப்புக் கருவித்தொகுப்பு, பயிற்சிகளுடன்; qos Desktop-இல் Wireshark.",
     "வலையமைப்புப் போக்குவரத்தைப் பிடிப்பதற்கும் Wi-Fi கண்காணிப்புக்கும் ரூட் தேவை. தாக்குதல் கருவித்தொகுப்புகள் சேர்க்கப்படவில்லை."),
    ("ai", "செயற்கை நுண்ணறிவு (AI)",
     "llama.cpp அல்லது Ollama கொண்டு திறந்த மொழி மாதிரிகளைக் கைபேசியிலேயே இயக்கலாம்; PyTorch, ONNX Runtime, NumPy, SciPy கொண்டு இயந்திரக் கற்றல். கணக்கும் இல்லை, கட்டண AI சேவையும் இல்லை.",
     "உள்ளூர் AI கருவித்தொகுப்பு: தேர்ந்த மாதிரி பதிவிறக்கப்பட்டு ஆயத்தமாக; சாதனத்திலேயே இயங்கும் VS Code நிரல் உதவியாளர்.",
     "சிறிய மாதிரிகள் மட்டும்: சுமார் 100 கோடி முதல் 400 கோடி அளவுருக்கள், 4 முதல் 8 GB RAM தேவை. மேகச் சேவைகளை விடப் பதில்கள் மெதுவாக வரும்."),
]


def beyond_rows():
    return "\n".join(
        f'<div class="cap-row" id="{key}"><h3>{name}</h3>'
        f'<div class="today"><span class="label">இன்று</span><p>{today}</p></div>'
        f'<div class="coming"><span class="label">வருகிறது</span><p>{coming}</p></div>'
        f'<div class="limits"><span class="label">வரம்புகள்</span><p>{limits}</p></div></div>'
        for key, name, today, coming, limits in BEYOND
    )


def beyond_tiles():
    return "\n".join(f'<a class="tile" href="@L@features/#{key}">{name}</a>' for key, name, *_ in BEYOND)


AUDIENCE = """
<div class="grid">
  <div class="card"><h3>மாணவர்கள்</h3><p>கணினி ஆய்வகத்துக்குக் காத்திருக்காமல், கையில் உள்ள கைபேசியிலேயே Python, C, Java, Rust கற்கலாம்.</p></div>
  <div class="card"><h3>நிரலாக்கம் கற்கும் தமிழர்கள்</h3><p>இ-தமிழில் தமிழிலேயே நிரல் எழுதுங்கள்; அதே முனையத்திலிருந்து பிற மொழிகளுக்கும் செல்லுங்கள்.</p></div>
  <div class="card"><h3>ஆசிரியர்களும் கல்லூரிகளும்</h3><p>கைபேசிகளிலும் டேப்லெட்டுகளிலும் நிரலாக்க வகுப்புகளை நடத்துங்கள். ஒவ்வொரு மாணவருக்கும் ஒரே கருவிகள், ஒரே அமைப்பு.</p></div>
  <div class="card"><h3>பணிபுரியும் நிரலாளர்கள்</h3><p>மேசையை விட்டு விலகியிருக்கும்போதும் பிழை திருத்தலாம், கிளையைச் சரிபார்க்கலாம், commit அனுப்பலாம், SSH வழியே சேவையகத்தை அணுகலாம்.</p></div>
  <div class="card"><h3>இ-தமிழ் நிரலாளர்கள்</h3><p>உண்மையான தொகுப்பியைக் கொண்டு இ-தமிழ் நிரல்கள், கூறுகள், சேவையகங்களை ஆண்ட்ராய்டிலேயே கட்டிச் சோதிக்கலாம்.</p></div>
  <div class="card"><h3>உருவாக்குநர்களும் ஆர்வலர்களும்</h3><p>கைபேசிப் பணிகளைத் தானியக்கமாக்குங்கள், சிறு சேவையகங்களை இயக்குங்கள், Wi-Fi வழியே பலகைகளுடன் பேசுங்கள், லினக்ஸை ஒரே செயலிக்குள் பாதுகாப்பாக ஆராயுங்கள்.</p></div>
</div>"""

REQUIREMENTS = """
<table class="table">
  <thead><tr><th></th><th>குறைந்தபட்சம்</th><th>பரிந்துரைக்கப்படுவது</th></tr></thead>
  <tbody>
    <tr><th>ஆண்ட்ராய்டு</th><td class="strong" data-label="குறைந்தபட்சம்">7.0 (Nougat)</td><td data-label="பரிந்துரை">10 அல்லது அதற்குப் புதியது</td></tr>
    <tr><th>செயலகம்</th><td class="strong" data-label="குறைந்தபட்சம்">ARM (32 அல்லது 64-பிட்) அல்லது x86</td><td data-label="பரிந்துரை">64-பிட் ARM (arm64-v8a) — 2017 முதல் வந்த ஏறக்குறைய எல்லாக் கைபேசிகளிலும் உள்ளது. இ-தமிழ் கருவிகளுக்கு இது தேவை.</td></tr>
    <tr><th>நினைவகம் (RAM)</th><td class="strong" data-label="குறைந்தபட்சம்">3 GB</td><td data-label="பரிந்துரை">VS Code, Rust கட்டுமானங்கள், qos Desktop-க்கு 4 GB அல்லது அதற்கு மேல்; உள்ளூர் AI மாதிரிகளுக்கு 6 முதல் 8 GB</td></tr>
    <tr><th>காலி இடம்</th><td class="strong" data-label="குறைந்தபட்சம்">4 GB</td><td data-label="பரிந்துரை">8 GB அல்லது அதற்கு மேல். நிரலாக்கக் கருவித்தொகுப்பு நிறுவிய பின் சுமார் 2.3 GB; qos Desktop-இன் XFCE மேலும் சுமார் 0.6 GB.</td></tr>
    <tr><th>இணையம்</th><td class="strong" data-label="குறைந்தபட்சம்">முதல் முறை திறக்க: சுமார் 500 MB</td><td data-label="பரிந்துரை">அமைப்புக்கு Wi-Fi. அதன் பின் qos இணையம் இல்லாமலும் இயங்கும்.</td></tr>
    <tr><th>உள்ளீடு</th><td class="strong" data-label="குறைந்தபட்சம்">திரை விசைப்பலகை</td><td data-label="பரிந்துரை">Bluetooth அல்லது USB விசைப்பலகை — குறிப்பாக டேப்லெட்டில்; qos Desktop-க்கு ஒரு சுட்டி</td></tr>
  </tbody>
</table>
<p class="small">சேமிப்பு, பதிவிறக்க அளவுகள் தற்போதைய தொகுப்புப் பதிப்புகளிலிருந்து அளக்கப்பட்டவை; அவை புதுப்பிக்கப்படும்போது மாறும். நினைவக அளவுகள் வழிகாட்டுதல் மட்டுமே, கட்டாய வரம்புகள் அல்ல.</p>"""

STAGES = """
<div class="roadmap">
  <div class="stage"><span class="tag">இப்போது கிடைக்கிறது · v0.2</span><h3>இயங்கும் நிரலாக்கக் கணினி</h3><ul>
    <li>முழு Termux தொகுப்புத் திரட்டுடன் லினக்ஸ் முனையம்</li>
    <li>git, clang, make, Python, Rust, Java 17 — ஒருமுறை அமைப்பு</li>
    <li>செயலிக்குள்ளேயே VS Code, தானாக உள்நுழைவுடன்</li>
    <li>qos Desktop: வரைகலைச் செயலிகளுக்கான XFCE மேசைத்தளம் <span class="new">புதியது</span></li>
    <li>இ-தமிழ் தொகுப்பியும் அதன் நூலகமான நூலகமும் (64-பிட் ARM)</li>
    <li>GitHub-இலும் qos F-Droid களஞ்சியத்திலும் கையொப்பமிட்ட வெளியீடுகள்</li></ul></div>
  <div class="stage"><span class="tag amber">அடுத்து</span><h3>அன்றாடப் பயன்பாட்டை எளிதாக்குதல்</h3><ul>
    <li>ஆண்ட்ராய்டுக்கென்றே கட்டிய இ-தமிழ் — இ-தமிழ் நிரல்கள் இணையதளங்களையும் API-களையும் பெயரால் அணுக</li>
    <li>முதல் முறை எந்தக் கருவிகளை நிறுவுவது என்று நீங்களே தேர்வு செய்யுங்கள்</li>
    <li>செயலியின் சொந்தத் திரைகள் தமிழில்</li>
    <li>VS Code அமைப்புகள்: திறக்கும்போதே தொடங்குதல், port தேர்வு</li></ul></div>
  <div class="stage"><span class="tag violet">திட்டமிடப்பட்டவை</span><h3>எல்லா வகைப் பணிகளுக்கும் கருவித்தொகுப்புகள்</h3><ul>
    <li><strong>நோக்கத்துக்கேற்ற அமைப்பு:</strong> முதல் முறை நீங்கள் என்ன செய்ய வந்தீர்கள் என்று தேர்ந்தெடுங்கள்; அதற்கேற்ற கருவித்தொகுப்பை qos நிறுவும்</li>
    <li>ஆண்ட்ராய்டு செயலிகள், விளையாட்டுகள், அசைவூட்டம், திரைப்படம், IoT, பாதுகாப்பு, உள்ளூர் AI ஆகியவற்றுக்கான கருவித்தொகுப்புகள்</li>
    <li>சாதனத்துக்கான qos இணைப்புகள்: அறிவிப்புகள், உணரிகள், கேமரா, விட்ஜெட்டுகள், தொடக்கத்திலேயே இயங்கும் நிரல்கள்</li>
    <li>Termux தொகுக்காத கருவிகளுக்காக முழுமையான Debian சூழல்</li></ul></div>
  <div class="stage"><span class="tag grey">ஆராய்கிறோம்</span><h3>நாங்கள் பரிசீலிக்கும் யோசனைகள்</h3><ul>
    <li>qos Desktop-ஐ qos-க்குள்ளேயே இணைத்தல்: இரண்டுக்குப் பதில் ஒரே செயலி</li>
    <li>ரூட் இல்லாமல் USB வழியே பலகைகளில் நிரலேற்றுதல்; கைபேசியிலிருந்தே Arduino-வில் இ-தமிழ்</li>
    <li>வகுப்பறைகளுக்கான ஆயத்தப் பாடங்கள்</li>
    <li>தமிழிலும் ஆங்கிலத்திலும் ஆவணங்கள்</li></ul></div>
</div>"""

FDROID_STEPS = """
<ol>
  <li>ஒரு F-Droid செயலியை நிறுவுங்கள்: <a href="https://f-droid.org">F-Droid</a>, Droid-ify அல்லது Neo Store.</li>
  <li>உங்கள் கைபேசியில் <a data-fdroid-link href="fdroidrepos://qos.ae/fdroid/repo?fingerprint=@FP@">qos களஞ்சியத்தைச் சேர்</a> என்பதைத் தொடுங்கள், அல்லது கைமுறையாகச் சேருங்கள்:
    <span class="url" data-fdroid-url>https://qos.ae/fdroid/repo</span>இந்தக் கைரேகையைச் சரிபாருங்கள்:<span class="url">@FP@</span></li>
  <li><strong>qos</strong> எனத் தேடி நிறுவுங்கள். மேசைத்தளம் வேண்டுமெனில் <strong>qos Desktop</strong>-ஐயும் நிறுவுங்கள்.</li>
</ol>"""

HOME = f"""
<header class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">இலவசம், திறந்த மூலம் · ஆண்ட்ராய்டு 7 மற்றும் புதியவை</p>
      <h1>உங்கள் கைபேசியே ஒரு நிரலாக்கக் கணினி.</h1>
      <p class="sub">லினக்ஸ் முனையம், VS Code, தொகுப்பிகள், மேசைத்தளம், இ-தமிழ் கருவிகள் — அனைத்தையும் qos உங்கள் ஆண்ட்ராய்டு கைபேசியிலோ டேப்லெட்டிலோ தருகிறது. மடிக்கணினி இல்லாமல், கணக்கு இல்லாமல், எங்கும் உண்மையான மென்பொருளை எழுதி, கட்டி, இயக்குங்கள்.</p>
      <div class="cta"><a class="btn primary" href="@L@download/">qos பெறுக</a><a class="btn ghost" href="@L@features/">உள்ளே என்ன இருக்கிறது</a></div>
      <div class="facts"><span>GPLv3</span><span>கணக்கு இல்லை, விளம்பரம் இல்லை, கண்காணிப்பு இல்லை</span><span>அமைத்த பின் இணையம் இல்லாமலும் இயங்கும்</span><span>ரூட் தேவையில்லை</span></div>
    </div>
    <div class="art">{FIG.format(cls="phone", name="phone-etamil", alt="கைபேசியில் தமிழில் எழுதிய இ-தமிழ் நிரல்", w=360, h=720)}</div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="feature flip">
      <div class="media">{fig("tablet-vscode", "டேப்லெட்டில் qos-க்குள் இயங்கும் VS Code", True)}</div>
      <div><p class="eyebrow">திருத்தி</p><h2>செயலிக்குள்ளேயே VS Code</h2>
        <p>முழுமையான VS Code கைபேசியிலேயே இயங்குகிறது; பக்கப் பட்டியிலிருந்து திறக்கலாம்: கோப்பு மரம், Open VSX நீட்சிகள், கீழே முனையம். மேகக்கணினி இல்லை, உள்நுழைவு இல்லை; நீங்கள் அனுப்பும் வரை உங்கள் நிரல் கைபேசியை விட்டு வெளியேறாது.</p>
        <p class="note">விசைப்பலகையுடன் கூடிய டேப்லெட்டில் சிறப்பாக இருக்கும். கைபேசியில் முனையமும் உரைத் திருத்தியும் பெரும்பாலும் விரைவானவை.</p>
        <a class="more" href="@L@docs/#vscode">qos-இல் VS Code எப்படி இயங்குகிறது →</a></div>
    </div>
    <div class="feature">
      <div class="media">{fig("tablet-desktop", "டேப்லெட்டில் qos Desktop-இல் XFCE மேசைத்தளம்", True)}</div>
      <div><p class="eyebrow">மேசைத்தளம் <span class="new">0.2-இல் புதியது</span></p><h2>தேவைப்படும்போது லினக்ஸ் மேசைத்தளம்</h2>
        <p>பக்கப் பட்டியில் Desktop-ஐத் தொட்டால், qos தன் துணைத் திரையான qos Desktop-இல் XFCE-ஐத் திறக்கும். வரைகலைக் கருவிகளை இயக்குங்கள்: வரைதலுக்கும் அசைவூட்டத்துக்கும் Krita, Inkscape; காணொளிக்கு Kdenlive; விளையாட்டுகளுக்கு Godot; வலையமைப்புகளுக்கு Wireshark.</p>
        <p class="note">qos Desktop அதே மூலத்திலிருந்து வரும் இரண்டாவது செயலி; அதே சாவியால் கையொப்பமிடப்பட்டு qos-இன் ஒரு பகுதியாக இயங்குகிறது. முதல் தொடக்கம் சுமார் 100 MB பதிவிறக்கும்.</p>
        <a class="more" href="@L@docs/#desktop">மேசைத்தளத்தைத் தொடங்குங்கள் →</a></div>
    </div>
    <div class="feature flip">
      <div class="media">{fig("phone-terminal", "கைபேசியில் qos முனையம்")}</div>
      <div><p class="eyebrow">முனையம்</p><h2>உண்மையான லினக்ஸ் முனையம்</h2>
        <p>qos, Termux-ஐ அடிப்படையாகக் கொண்டது; அதனால் முழு Termux தொகுப்புத் திரட்டும் இயங்கும் — ஆயிரக்கணக்கான தொகுப்புகள், <code>pkg install</code> கொண்டு நிறுவலாம். இ-தமிழ் உடன் வருகிறது: தமிழிலேயே நிரலாக்கம் கற்று, அதே முனையத்தில் Python, C, Rust-க்குச் செல்லுங்கள்.</p>
        <a class="more" href="https://etamil.in/ta/">இ-தமிழை etamil.in-இல் கற்றுக்கொள்ளுங்கள் →</a></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">உள்ளே என்ன இருக்கிறது</p><h2>மடிக்கணினியில் நீங்கள் நிறுவும் அதே கருவிகள்</h2>
    <p class="intro">முதல் முறை திறக்கும்போதே அமைகின்றன; அல்லது ஆயிரக்கணக்கான தொகுப்புகளிலிருந்து ஒரு <code>pkg install</code> தொலைவில்.</p>
    <div class="chip-group"><h3>முதல் முறை திறக்கும்போதே நிறுவப்படுபவை</h3><div class="chips">
      <span class="chip on">git</span><span class="chip on">clang / C / C++</span><span class="chip on">make</span><span class="chip on">Python</span><span class="chip on">Rust</span><span class="chip on">Java 17</span><span class="chip on">Node.js</span><span class="chip on">VS Code (code-server)</span><span class="chip on">இ-தமிழ்</span><span class="chip on">நூலகம்</span></div></div>
    <div class="chip-group"><h3>ஒரு கட்டளை தொலைவில்</h3><div class="chips">
      <span class="chip">Kotlin</span><span class="chip">Gradle</span><span class="chip">Go</span><span class="chip">PHP</span><span class="chip">Ruby</span><span class="chip">PostgreSQL</span><span class="chip">SQLite</span><span class="chip">Redis</span><span class="chip">nginx</span><span class="chip">OpenSSH</span><span class="chip">neovim</span><span class="chip">ffmpeg</span><span class="chip">nmap</span><span class="chip">llama.cpp</span><span class="chip">XFCE</span><span class="chip">Krita</span><span class="chip">Godot</span></div></div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">யாருக்காக</p><h2>கைபேசியும், கட்ட ஒரு யோசனையும் உள்ள எவருக்கும்</h2>
    <p class="intro">நிரலாக்கம் கற்க விரும்பும் பெரும்பாலானோரிடம் ஏற்கனவே ஓர் ஆண்ட்ராய்டு கைபேசி இருக்கிறது; மடிக்கணினி இருப்பவர்கள் மிகக் குறைவு. qos அவர்களுக்காக — தங்கள் கருவிகள் எப்போதும் கையருகே இருக்க வேண்டும் என்று விரும்பும் எவருக்காகவும்.</p>
    {AUDIENCE}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">நிரலுக்கு அப்பால்</p><h2>செயலிகள், விளையாட்டுகள், கார்ட்டூன்கள், திரைப்படங்கள், IoT, பாதுகாப்பு, AI</h2>
    <p class="intro">qos ஒரு நிரல் திருத்தி மட்டுமல்ல. ஒவ்வொரு வகைப் பணியும் இன்று எப்படி இருக்கிறது, திட்டப் பாதை எதைச் சேர்க்கிறது என்று பாருங்கள்.</p>
    <div class="tiles">{beyond_tiles()}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">நம்பிக்கை</p><h2>திறந்த, தனியுரிமை காக்கும், சரிபார்க்கக்கூடிய</h2>
    <div class="grid four">
      <div class="card"><h3>திறந்த மூலம்</h3><p>ஒவ்வொரு வரியும் GNU GPL v3 உரிமத்தின் கீழ் பொதுவில் உள்ளது; Termux, Termux:X11 ஆகியவற்றை அடிப்படையாகக் கொண்டது.</p></div>
      <div class="card"><h3>கணக்கு இல்லை</h3><p>உள்நுழைவு, விளம்பரம், பகுப்பாய்வு, தொலைஅளவீடு எதுவும் இல்லை. இந்த இணையதளம் குக்கீகளை அமைப்பதில்லை.</p></div>
      <div class="card"><h3>கையொப்பமிட்ட வெளியீடுகள்</h3><p>ஒவ்வொரு APK-யும் qos சாவியாலும், F-Droid களஞ்சியம் தனிச் சாவியாலும் கையொப்பமிடப்படுகின்றன; இரண்டின் கைரேகைகளும் வெளியிடப்பட்டுள்ளன.</p></div>
      <div class="card"><h3>திறந்த முறையில் கட்டப்படுகிறது</h3><p>வெளியீடுகள், குறிக்கப்பட்ட மூல நிரலிலிருந்து பொது GitHub பணிப்பாய்வுகளால் SHA-256 சரிபார்ப்புத் தொகைகளுடன் கட்டப்படுகின்றன.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">தொடங்குங்கள்</p><h2>மூன்று படிகள்</h2>
    <div class="steps">
      <div class="card step"><h3>qos களஞ்சியத்தைச் சேருங்கள்</h3><p>F-Droid-இல் qos களஞ்சியத்தைச் சேர்த்து அதன் கைரேகையைச் சரிபாருங்கள். அல்லது GitHub-இலிருந்து APK-ஐப் பதிவிறக்குங்கள்.</p></div>
      <div class="card step"><h3>qos-ஐ நிறுவித் திறங்கள்</h3><p>முதல் முறை திறக்கும்போது qos தன் கருவிகளை அமைக்கிறது. Wi-Fi பயன்படுத்துங்கள்: சுமார் 500 MB பதிவிறக்கும்.</p></div>
      <div class="card step"><h3>கட்டத் தொடங்குங்கள்</h3><p>முனையத்தில் தட்டச்சு செய்யுங்கள், அல்லது VS Code, Desktop-க்கு இடப்புறமிருந்து உள்ளே இழுங்கள்.</p></div>
    </div>
    <p style="margin-top:24px"><a class="btn primary" href="@L@download/">பதிவிறக்கப் பக்கத்துக்குச் செல்லுங்கள்</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="band"><div><h2>qos எங்கே செல்கிறது</h2><p>ஒவ்வொரு மாதமும் சிறு வெளியீடுகள்: எல்லா வகைப் பணிகளுக்கும் கருவித்தொகுப்புகள், நோக்கத்துக்கேற்ற அமைப்பு.</p></div><a class="btn ghost" href="@L@roadmap/">திட்டப் பாதையைப் பாருங்கள்</a></div>
  </div>
</section>
"""

FEATURES = f"""
<header class="page-hero"><div class="wrap"><p class="eyebrow">வசதிகள்</p><h1>ஒரு நிரலாக்கக் கணினிக்குத் தேவையான அனைத்தும்</h1><p>லினக்ஸ் முனையம், உண்மையான தொகுப்பிகள், VS Code, மேசைத்தளம், இ-தமிழ் — உங்கள் கைபேசியிலோ டேப்லெட்டிலோ ஒரே செயலியில்.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="feature">
      <div class="media">{fig("phone-terminal", "கைபேசியில் qos முனையம்")}</div>
      <div><p class="eyebrow">முனையம்</p><h2>உண்மையான லினக்ஸ் முனையம்</h2>
        <p>qos, Termux-ஐ அடிப்படையாகக் கொண்டது; அதனால் முழு Termux தொகுப்புத் திரட்டும் இயங்கும்: ஆயிரக்கணக்கான தொகுப்புகள், <code>pkg install</code> கொண்டு நிறுவலாம். கூடுதல் விசை வரிசை தொடுதிரையிலும் Esc, Ctrl, Tab, அம்புக்குறி விசைகளைத் தருகிறது.</p>
        <p>git, clang, make, Python, Rust, Java 17 ஆகியவை VS Code, இ-தமிழ் உடன் qos முதல் முறை திறக்கும்போதே அமைகின்றன.</p></div>
    </div>
    <div class="feature flip">
      <div class="media">{fig("tablet-vscode", "டேப்லெட்டில் qos-க்குள் இயங்கும் VS Code", True)}</div>
      <div><p class="eyebrow">திருத்தி</p><h2>செயலிக்குள்ளேயே VS Code</h2>
        <p>code-server கைபேசியிலேயே இயங்கி, பக்கப் பட்டியிலிருந்து திறக்கிறது. code-server-இன் சொந்தக் கடவுச்சொல்லைக் கொண்டு qos உங்களை உள்நுழைக்கிறது; கைபேசியில் உள்ள எந்தச் செயலியும் அது கேட்கும் port-ஐ அணுக முடியும் என்பதால் அந்தக் கடவுச்சொல்லை இயக்கத்திலேயே வைத்திருக்கிறது.</p>
        <p>நீட்சிகள் திறந்த நீட்சிப் பதிவகமான Open VSX-இலிருந்து வருகின்றன.</p></div>
    </div>
    <div class="feature">
      <div class="media">{fig("tablet-desktop", "டேப்லெட்டில் qos Desktop-இல் XFCE மேசைத்தளம்", True)}</div>
      <div><p class="eyebrow">மேசைத்தளம் <span class="new">0.2-இல் புதியது</span></p><h2>qos Desktop</h2>
        <p>Termux:X11-இலிருந்து கட்டப்பட்ட துணைத் திரையான qos Desktop-இல் XFCE மேசைத்தளம். இது qos-இன் ஒரு பகுதியாக இயங்குவதால், ஆண்ட்ராய்டு இரண்டையும் ஒரே செயலியாகக் கருதுகிறது. சாளரங்கள் உள்ள எதற்கும் பயன்படுத்துங்கள்: Krita, Inkscape, GIMP, Kdenlive, Shotcut, Audacity, Godot, Wireshark, Firefox.</p>
        <p class="note">கைபேசிகளில் கணினி வரைகலை இயக்கிகள் இல்லை; அதனால் கனமான 3D மெதுவாக இருக்கும். சுட்டியோ தொடுதிண்டுடன் கூடிய விசைப்பலகையோ உதவும்.</p></div>
    </div>
    <div class="feature flip">
      <div class="media">{fig("phone-etamil", "கைபேசியில் தமிழில் எழுதிய இ-தமிழ் நிரல்")}</div>
      <div><p class="eyebrow">இ-தமிழ்</p><h2>தமிழில் நிரலாக்கம்</h2>
        <p>இ-தமிழ் தொகுப்பியும் அதன் நிலையான நூலகமான நூலகமும் முதல் முறை திறக்கும்போதே நிறுவப்படுகின்றன. இ-தமிழ் நிரல்கள் கோப்புகளைப் படிக்கும், SQLite பயன்படுத்தும், இணைய API-களை அழைக்கும், சேவையகங்களை இயக்கும்.</p>
        <p class="note">qos தற்போது இ-தமிழின் பொது லினக்ஸ் பதிப்பை வழங்குகிறது; அதில் இணைய முகவரிகளைப் பெயரால் தேடுவது ஆண்ட்ராய்டில் இயங்காமல் போகலாம். ஆண்ட்ராய்டுக்கென்றே கட்டிய பதிப்பு திட்டப் பாதையில் அடுத்தது.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="beyond">
  <div class="wrap">
    <p class="eyebrow">நிரலுக்கு அப்பால்</p><h2>செயலிகள், விளையாட்டுகள், கார்ட்டூன்கள், திரைப்படங்கள், IoT, பாதுகாப்பு, AI</h2>
    <p class="intro">ஒவ்வொரு வகைப் பணியும் இன்று qos-இல் எப்படி இருக்கிறது, திட்டப் பாதை எதைச் சேர்க்கிறது, அதன் வரம்புகள் என்ன — தொகுப்புத் திரட்டுகளில் உண்மையில் உள்ளவற்றின் அடிப்படையில்.</p>
    <div class="cap">{beyond_rows()}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">யாருக்காக</p><h2>கற்பவர்களுக்கும் உருவாக்குநர்களுக்குமாகக் கட்டப்பட்டது</h2>
    {AUDIENCE}
  </div>
</section>
"""

DOWNLOAD = f"""
<header class="page-hero"><div class="wrap"><p class="eyebrow">பதிவிறக்கம்</p><h1>qos பெறுக</h1><p>qos இலவசம். எப்படி நிறுவுவது என்று தேர்ந்தெடுங்கள்; F-Droid பரிந்துரைக்கப்படுகிறது, ஏனெனில் புதுப்பிப்புகள் தாமாகவே வரும்.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="grid">
      <div class="card recommended"><span class="tag">பரிந்துரை</span><h3>F-Droid களஞ்சியம்</h3><p>ஒரு F-Droid செயலியில் qos களஞ்சியத்தை ஒருமுறை சேருங்கள்.</p>
        <ul class="pros"><li class="plus">qos, qos Desktop இரண்டுக்கும் தானியங்கிப் புதுப்பிப்புகள்</li><li class="plus">கைரேகையுடன் சரிபார்க்கப்படும் கையொப்பமிட்ட அட்டவணை</li><li class="minus">ஒரு F-Droid செயலி தேவை</li></ul>
        {FDROID_STEPS}</div>
      <div class="card"><span class="tag grey">நேரடி</span><h3>GitHub வெளியீடுகள்</h3><p>APK-ஐப் பதிவிறக்கி நீங்களே நிறுவுங்கள்.</p>
        <ul class="pros"><li class="plus">கூடுதல் செயலி தேவையில்லை</li><li class="plus">ஒவ்வொரு வெளியீட்டிலும் SHA-256 சரிபார்ப்புத் தொகைகள்</li><li class="minus">கைமுறையாகப் புதுப்பிக்க வேண்டும்</li></ul>
        <ol><li><a href="https://github.com/Maruff/qos/releases/latest">சமீபத்திய qos வெளியீட்டைத்</a> திறங்கள்.</li><li>உங்கள் கைபேசிக்கான APK-ஐப் பதிவிறக்குங்கள் (கீழே பாருங்கள்).</li><li>அதைத் திறந்து, ஆண்ட்ராய்டு கேட்கும்போது உலாவிக்குச் செயலிகளை நிறுவ அனுமதி கொடுங்கள்.</li></ol></div>
      <div class="card"><span class="tag grey">புதுப்பிப்பி</span><h3>Obtainium</h3><p>GitHub வெளியீடுகளை Obtainium பின்தொடரட்டும்.</p>
        <ul class="pros"><li class="plus">F-Droid இல்லாமலேயே GitHub-இலிருந்து புதுப்பிப்புகள்</li><li class="minus">அமைக்க இன்னொரு செயலி</li></ul>
        <ol><li><a href="https://github.com/ImranR98/Obtainium">Obtainium</a>-ஐ நிறுவுங்கள்.</li><li><code>https://github.com/Maruff/qos</code>-ஐ ஒரு செயலி மூலமாகச் சேருங்கள்.</li></ol></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">எந்த APK</p><h2>உங்கள் செயலகத்துக்கான APK-ஐத் தேர்ந்தெடுங்கள்</h2>
    <p class="intro">F-Droid உங்களுக்காகத் தேர்ந்தெடுக்கும். GitHub-இலிருந்து என்றால், கைபேசியின் செயலகத்தின்படி தேர்ந்தெடுங்கள்; உறுதியாகத் தெரியவில்லை என்றால், ஏறக்குறைய நிச்சயம் arm64-v8a.</p>
    <table class="table"><thead><tr><th>கோப்பு</th><th>எதற்கு</th></tr></thead><tbody>
      <tr><th><code>qos-…-arm64-v8a.apk</code></th><td data-label="எதற்கு">2017 முதல் வந்த ஏறக்குறைய எல்லாக் கைபேசிகளும் டேப்லெட்டுகளும். பரிந்துரை.</td></tr>
      <tr><th><code>qos-…-armeabi-v7a.apk</code></th><td data-label="எதற்கு">பழைய, விலை குறைந்த 32-பிட் கைபேசிகள். இதற்கு இன்னும் இ-தமிழ் கருவிகள் இல்லை.</td></tr>
      <tr><th><code>qos-…-x86_64.apk</code></th><td data-label="எதற்கு">Chromebook-கள், ஆண்ட்ராய்டு போலிகள் (emulator).</td></tr>
      <tr><th><code>qos-…-x86.apk</code></th><td data-label="எதற்கு">பழைய 32-பிட் Intel சாதனங்கள்.</td></tr>
    </tbody></table>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="feature">
      <div class="media">{fig("tablet-desktop", "qos Desktop-இல் XFCE மேசைத்தளம்", True)}</div>
      <div><p class="eyebrow">இணைப்பு</p><h2>qos Desktop</h2>
        <p>சாளரங்களும் சுட்டியும் வேண்டுமா? qos-க்குப் பின் qos Desktop-ஐ நிறுவுங்கள்: அதே F-Droid களஞ்சியத்திலிருந்து, அல்லது GitHub-இலிருந்து <a href="https://github.com/Maruff/qos-desktop/releases/latest">qos-desktop.apk</a>. பின் qos பக்கப் பட்டியில் Desktop-ஐத் தொடுங்கள்.</p>
        <p class="note">qos Desktop, இதே மூலங்களிலிருந்து வரும் qos உடன் மட்டுமே இயங்கும்; இரண்டும் qos சாவியால் கையொப்பமிடப்பட்டிருக்க வேண்டும்.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="verify">
  <div class="wrap">
    <p class="eyebrow">சரிபார்ப்பு</p><h2>நீங்கள் நிறுவுவதைச் சரிபாருங்கள்</h2>
    <p class="intro">ஒவ்வொரு வெளியீட்டிலும் <code>sha256sums.txt</code>-இல் SHA-256 சரிபார்ப்புத் தொகைகள் உள்ளன. qos-க்குக் கையொப்பமிடும் சான்றிதழ்கள் இவை:</p>
    <table class="table"><tbody>
      <tr><th>qos, qos Desktop APK-கள்</th><td><code>379DA39A198B76D7AE4733C8FC78648CB509D2C1174D03E64442C9337FDEF8DA</code></td></tr>
      <tr><th>qos F-Droid களஞ்சியம்</th><td><code>@FP@</code></td></tr>
    </tbody></table>
    <p class="small">Android SDK இருந்தால்: <code>apksigner verify --print-certs qos-….apk</code> APK-இன் SHA-256 சான்றிதழ்ச் சுருக்கத்தைக் காட்டும்.</p>
  </div>
</section>

<section id="requirements">
  <div class="wrap">
    <p class="eyebrow">தேவைகள்</p><h2>உங்கள் சாதனத்துக்கு என்ன வேண்டும்</h2>
    {REQUIREMENTS}
    <div class="notes">
      <div class="note"><strong>qos, Termux-க்குப் பதிலாக நிறுவப்படும்.</strong> எல்லா Termux தொகுப்புகளும் இயங்குவதற்காக அது Termux-இன் தொகுப்புப் பெயரையே பயன்படுத்துகிறது. எனவே இரண்டையும் ஒரே நேரத்தில் நிறுவ முடியாது; Termux இணைப்புச் செயலிகளும் qos உடன் இயங்காது. முதலில் Termux-இல் தேவையானவற்றைக் காப்புப்பிரதி எடுத்துக்கொள்ளுங்கள்.</div>
      <div class="note"><strong>Google Play-இல் இல்லை.</strong> பதிவிறக்கிய நிரல்களை இயக்கும் செயலிகளை Play அனுமதிப்பதில்லை; ஒரு நிரலாக்கக் கணினி செய்ய வேண்டியது அதுதான்.</div>
    </div>
  </div>
</section>
"""

DOCS = """
<header class="page-hero"><div class="wrap"><p class="eyebrow">ஆவணங்கள்</p><h1>qos-ஐப் பயன்படுத்துதல்</h1><p>முதல் முறை திறப்பதிலிருந்து மேசைத்தளம் வரை; ஏதாவது தவறினால் என்ன செய்வது.</p></div></header>

<section class="flush">
  <div class="wrap docs">
    <nav class="toc" aria-label="இந்தப் பக்கத்தில்">
      <a href="#first-launch">முதல் முறை</a><a href="#terminal">முனையம்</a><a href="#storage">உங்கள் கோப்புகள்</a><a href="#vscode">VS Code</a><a href="#desktop">qos Desktop</a><a href="#etamil">இ-தமிழ்</a><a href="#background">பணி நிற்காமல் இருக்க</a><a href="#updates">புதுப்பிப்புகள்</a><a href="#troubleshooting">சிக்கல் தீர்வு</a><a href="#faq">கேள்விகள்</a>
    </nav>
    <div class="doc">
      <section id="first-launch"><h2>முதல் முறை திறக்கும்போது</h2>
        <p>qos முதல் முறை திறக்கும்போது தன் அடிப்படை அமைப்பை நிறுவி, பின் <code>qos-setup</code>-ஐ இயக்குகிறது; அது git, clang, make, Python, Rust, Java 17, code-server, இ-தமிழ் ஆகியவற்றை நிறுவுகிறது. சுமார் 500 MB பதிவிறக்கும்; எனவே Wi-Fi பயன்படுத்தித் திரையை அணையாமல் வைத்திருங்கள். முடிந்ததும் முனையத்தில் <strong>Done</strong> தெரியும்.</p>
        <p>அமைப்பு இடையில் நின்றால், அடுத்த முறை தொடரும். எப்போது வேண்டுமானாலும் மீண்டும் இயக்கலாம்:</p><pre>qos-setup</pre></section>
      <section id="terminal"><h2>முனையம்</h2>
        <p>தொகுப்புத் திரட்டிலிருந்து எதையும் <code>pkg</code> கொண்டு நிறுவலாம்:</p><pre>pkg search postgres
pkg install postgresql</pre>
        <p>இடது ஓரத்திலிருந்து உள்ளே இழுத்தால் பக்கப் பட்டி: அமர்வுகள், விசைப்பலகை மாற்றி, VS Code, Desktop. கூடுதல் விசை வரிசையைக் காட்ட அல்லது மறைக்க விசைப்பலகைப் பொத்தானை நீண்ட நேரம் அழுத்துங்கள்.</p></section>
      <section id="storage"><h2>உங்கள் கோப்புகள்</h2>
        <p>உங்கள் திட்டங்கள் qos-இன் வீட்டுக் கோப்புறையில் இருக்கும். கைபேசியின் பகிர்ந்த சேமிப்பை (Downloads, Pictures, கேமரா காட்சிகள்) அணுக, ஒருமுறை இயக்குங்கள்:</p><pre>termux-setup-storage</pre><p>அது அனுமதி கேட்டு, அந்தக் கோப்புறைகளுக்கான இணைப்புகளுடன் <code>~/storage</code>-ஐ உருவாக்கும்.</p></section>
      <section id="vscode"><h2>VS Code</h2>
        <p>பக்கப் பட்டியில் <strong>VS Code</strong>-ஐத் தொடுங்கள். code-server இயங்கவில்லை என்றால் qos அதைப் பின்னணியில் தொடங்கி, <code>~/.config/code-server/config.yaml</code>-இல் உள்ள கடவுச்சொல்லைக் கொண்டு உங்களை உள்நுழைக்கும்.</p>
        <p>கடவுச்சொல் வேண்டுமென்றே இயக்கத்தில் உள்ளது: கைபேசியில் உள்ள எந்தச் செயலியும் 127.0.0.1:8080-ஐ அணுக முடியும், code-server கட்டளைகளை இயக்க முடியும். நீங்களே தொடங்க: <code>code-server</code>.</p></section>
      <section id="desktop"><h2>qos Desktop</h2>
        <p>qos F-Droid களஞ்சியத்திலிருந்து qos Desktop-ஐ நிறுவி, பக்கப் பட்டியில் <strong>Desktop</strong>-ஐத் தொடுங்கள். முதல் முறை qos, XFCE-ஐயும் (சுமார் 100 MB) <code>qos-x11</code> தொகுப்பையும் நிறுவி, மேசைத்தளத்தைத் திறக்கும். முனையத்திலிருந்து: <code>qos-desktop</code>.</p>
        <p>நிறுத்த: XFCE-இலிருந்து வெளியேறுங்கள், அல்லது qos Desktop அறிவிப்பில் Exit, அல்லது தொடங்கிய அமர்வில் Ctrl+C. முனையத்திலிருந்து தொடங்கும் வரைகலை நிரல்களுக்கு <code>DISPLAY=:1</code> தேவை.</p>
        <p>திரை கருப்பாகவே இருந்தால் அல்லது நிறங்கள் மாறித் தெரிந்தால், ஒரு விருப்பத்துடன் கைமுறையாகத் தொடங்குங்கள்:</p><pre>termux-x11 :1 -legacy-drawing -xstartup "xfce4-session"
termux-x11 :1 -force-bgra -xstartup "xfce4-session"</pre></section>
      <section id="etamil"><h2>இ-தமிழ்</h2>
        <p>இ-தமிழ் நிரலை மெய்நிகர் இயந்திரத்தில் இயக்கவும், இயக்காமலேயே சரிபார்க்கவும்:</p><pre>etamil --vm program.qmz
etamil --check program.qmz</pre>
        <p>நிலையான நூலகம் <code>$ETAMIL_PATH</code>-இல் உள்ளது; எனவே <code>இறக்கு "nUlakam/…"</code> எந்தக் கோப்புறையிலிருந்தும் இயங்கும். மொழியை <a href="https://etamil.in/ta/">etamil.in</a>-இல் கற்றுக்கொள்ளுங்கள்.</p></section>
      <section id="background"><h2>பணி நிற்காமல் இருக்க</h2>
        <p>ஆண்ட்ராய்டு 12 மற்றும் புதியவை பின்னணியில் நீண்ட நேரம் இயங்கும் கட்டுமானங்கள், VS Code, மேசைத்தளம் போன்றவற்றை நிறுத்தக்கூடும். ஆண்ட்ராய்டு 14 மற்றும் புதியவற்றில் Developer options-ஐ இயக்கி <strong>Disable child process restrictions</strong>-ஐச் செயல்படுத்துங்கள். qos-இன் மின்கலப் பயன்பாட்டை <strong>Unrestricted</strong> என அமைப்பதும் உதவும்.</p></section>
      <section id="updates"><h2>புதுப்பிப்புகள்</h2>
        <p>F-Droid களஞ்சியத்துடன், qos-உம் qos Desktop-உம் மற்ற செயலிகளைப் போலவே புதுப்பிக்கப்படும். qos-க்குள் உள்ள தொகுப்புகளைப் புதுப்பிக்க:</p><pre>pkg upgrade</pre></section>
      <section id="troubleshooting"><h2>சிக்கல் தீர்வு</h2>
        <details><summary>அமைப்பு பிழையுடன் நின்றது</summary><p>இணைய இணைப்பைச் சரிபார்த்து <code>qos-setup</code>-ஐ மீண்டும் இயக்குங்கள். ஒவ்வொரு படியையும் மீண்டும் இயக்கலாம்.</p></details>
        <details><summary>"qos Desktop is not installed"</summary><p>qos F-Droid களஞ்சியத்திலிருந்தோ qos-desktop GitHub வெளியீட்டிலிருந்தோ qos Desktop-ஐ நிறுவி, மீண்டும் Desktop-ஐத் தொடுங்கள்.</p></details>
        <details><summary>"Signature verification … failed"</summary><p>qos Desktop-உம் qos-x11 தொகுப்பும் வெவ்வேறு மூலங்களிலிருந்து வந்துள்ளன. இரண்டையும் Termux-இலிருந்து அல்ல, qos வெளியீடுகளிலிருந்தே நிறுவுங்கள்.</p></details>
        <details><summary>VS Code திறக்கவில்லை</summary><p>பிழையைப் பார்க்க முனையத்தில் <code>code-server</code> இயக்குங்கள். அது நிறுவப்படவில்லை என்றால் <code>qos-setup</code> இயக்குங்கள்.</p></details>
      </section>
      <section id="faq"><h2>கேள்விகள்</h2>
        <details><summary>qos இலவசமா?</summary><p>ஆம். qos, GNU GPL v3 உரிமத்தின் கீழ் உள்ள கட்டற்ற மென்பொருள்; விளம்பரங்களோ, செயலிக்குள் வாங்குதல்களோ, கணக்கோ இல்லை.</p></details>
        <details><summary>qos-க்கு ரூட் தேவையா?</summary><p>இல்லை. எல்லாமே செயலியின் சொந்தச் சேமிப்பிடத்துக்குள், சாதாரண செயலி அனுமதிகளுடன் இயங்குகின்றன.</p></details>
        <details><summary>qos, Termux-இலிருந்து எப்படி வேறுபடுகிறது?</summary><p>qos, Termux-ஐ அடிப்படையாகக் கொண்டு அதன் தொகுப்புத் திரட்டைத் தக்க வைத்துக்கொள்கிறது. அதனுடன் முழுக் கருவித்தொகுப்பின் ஒருமுறை அமைப்பு, செயலிக்குள்ளேயே VS Code, qos Desktop, இ-தமிழ் ஆகியவற்றைச் சேர்க்கிறது — எந்த அமைப்பும் இல்லாமலேயே புதிய கைபேசி நிரலாக்கக் கணினியாகிறது.</p></details>
        <details><summary>Termux-ஐயும் வைத்திருக்கலாமா?</summary><p>முடியாது. எல்லா Termux தொகுப்புகளும் இயங்குவதற்காக qos, Termux-இன் தொகுப்புப் பெயரையே பயன்படுத்துகிறது; அந்தப் பெயரில் ஒரு செயலியை மட்டுமே ஆண்ட்ராய்டு அனுமதிக்கும்.</p></details>
        <details><summary>qos ஏன் Google Play-இல் இல்லை?</summary><p>செயலிகள் சமீபத்திய ஆண்ட்ராய்டு பதிப்புகளை இலக்காகக் கொள்ள வேண்டும் என்று Play கோருகிறது; அவை பதிவிறக்கிய நிரல்களை ஒரு செயலி இயக்க அனுமதிப்பதில்லை. நிரலாக்கக் கணினி செய்ய வேண்டியதே அதுதான்.</p></details>
      </section>
    </div>
  </div>
</section>
"""

ROADMAP = f"""
<header class="page-hero"><div class="wrap"><p class="eyebrow">திட்டப் பாதை</p><h1>qos இப்போது எங்கே, எங்கே செல்கிறது</h1><p>qos ஒவ்வொரு மாதமும் சிறு வெளியீடுகளை வெளியிடுகிறது. இன்னும் வெளியிடப்படாதவை மாறக்கூடும்; மன்றத்தில் நீங்கள் சொல்வது வரிசையைத் தீர்மானிக்கிறது.</p></div></header>

<section class="flush">
  <div class="wrap">{STAGES}</div>
</section>

<section class="alt" id="purpose">
  <div class="wrap">
    <p class="eyebrow">திட்டமிடப்பட்டது</p><h2>நோக்கத்துக்கேற்ற அமைப்பு</h2>
    <p class="intro">qos முதிர்ச்சி அடைந்ததும், முதல் முறை திறக்கும்போது நீங்கள் என்ன செய்ய வந்தீர்கள் என்று கேட்டு, எல்லாவற்றுக்கும் பதிலாக அந்தப் பணிக்கான கருவித்தொகுப்பை மட்டும் நிறுவும்.</p>
    <div class="tiles four">
      <span class="tile">வணிகச் செயலிகள்<small>இ-தமிழ், Python, Node.js, PostgreSQL</small></span>
      <span class="tile">கைபேசிச் செயலிகள்<small>Kotlin, Gradle, Android கருவிகள்</small></span>
      <span class="tile">விளையாட்டுகள்<small>Godot, LÖVE, pygame</small></span>
      <span class="tile">இணையப் பாதுகாப்பு<small>nmap, radare2, jadx</small></span>
      <span class="tile">AI<small>llama.cpp, PyTorch</small></span>
      <span class="tile">திரைப்படம்<small>ffmpeg, Kdenlive</small></span>
      <span class="tile">IoT<small>MQTT, ESP32</small></span>
      <span class="tile">கற்றல்<small>Python, இ-தமிழ், பாடங்கள்</small></span>
    </div>
  </div>
</section>

<section id="releases">
  <div class="wrap">
    <p class="eyebrow">வெளியீட்டுக் குறிப்புகள்</p><h2>என்ன மாறியது</h2>
    <div class="grid two">
      <div class="card"><span class="tag">11 அக்டோபர் 2026</span><h3>qos 0.2, qos Desktop 0.1</h3><ul>
        <li>பக்கப் பட்டியில் உள்ள Desktop பொத்தான் qos Desktop-இல் XFCE மேசைத்தளத்தைத் திறக்கிறது; முதல் முறை அதை அமைக்கிறது.</li>
        <li>qos Desktop: qos சாவியால் கையொப்பமிடப்பட்ட Termux:X11 திரை; அதனால் qos-இன் ஒரு பகுதியாக இயங்குகிறது.</li>
        <li>இரண்டும் qos F-Droid களஞ்சியத்தில் உள்ளன.</li></ul>
        <p style="margin-top:10px"><a href="https://github.com/Maruff/qos/releases/tag/v0.2.0">qos 0.2.0</a> · <a href="https://github.com/Maruff/qos-desktop/releases/tag/v0.1.0">qos Desktop 0.1.0</a></p></div>
      <div class="card"><span class="tag grey">10 அக்டோபர் 2026</span><h3>qos 0.1</h3><ul>
        <li>முதல் வெளியீடு: git, clang, Python, Rust, Java 17, code-server, இ-தமிழ் ஆகியவற்றின் ஒருமுறை அமைப்புடன் Termux.</li>
        <li>செயலிக்குள்ளேயே VS Code, தானாக உள்நுழைவுடன்.</li>
        <li>நான்கு செயலக வகைகளுக்குக் கையொப்பமிட்ட APK-கள், qos F-Droid களஞ்சியம்.</li></ul>
        <p style="margin-top:10px"><a href="https://github.com/Maruff/qos/releases/tag/v0.1.0">qos 0.1.0</a></p></div>
    </div>
  </div>
</section>
"""

COMMUNITY = """
<header class="page-hero"><div class="wrap"><p class="eyebrow">சமூகம்</p><h1>கேளுங்கள், பகிருங்கள், qos-ஐ வடிவமைக்க உதவுங்கள்</h1><p>qos திறந்த முறையில் கட்டப்படுகிறது. கேள்விகள், யோசனைகள், பிழை அறிக்கைகள் அனைத்தும் வரவேற்கப்படுகின்றன — தமிழிலோ ஆங்கிலத்திலோ.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="grid two">
      <a class="card link" href="https://github.com/Maruff/qos/discussions"><span class="tag">மன்றம்</span><h3>கலந்துரையாடல்கள்</h3><p>கேள்விகள் கேளுங்கள், qos-இல் நீங்கள் கட்டியதைக் காட்டுங்கள், அடுத்து என்ன வர வேண்டும் என்று பரிந்துரையுங்கள்.</p><span class="go">மன்றத்தைத் திறங்கள் →</span></a>
      <a class="card link" href="https://github.com/Maruff/qos/issues"><span class="tag amber">சிக்கல்கள்</span><h3>சிக்கலைத் தெரிவியுங்கள்</h3><p>ஏதாவது வேலை செய்யவில்லையா? உங்கள் கைபேசி மாதிரி, ஆண்ட்ராய்டு பதிப்பு, நீங்கள் இயக்கியது ஆகியவற்றைச் சேர்த்துச் சொல்லுங்கள்.</p><span class="go">ஒரு issue திறங்கள் →</span></a>
      <a class="card link" href="https://github.com/Maruff/qos"><span class="tag violet">நிரல்</span><h3>பங்களியுங்கள்</h3><p>Pull request-கள், தமிழ் மொழிபெயர்ப்புகள், மேலும் பல சாதனங்களில் சோதனை — அனைத்தும் உதவும். நிரல் GPLv3 உரிமத்தில் உள்ளது.</p><span class="go">GitHub-இல் qos →</span></a>
      <a class="card link" href="https://etamil.in/ta/"><span class="tag grey">மொழி</span><h3>இ-தமிழ்</h3><p>qos உடன் வரும் தமிழ் நிரலாக்க மொழி — அதன் வழிகாட்டி, எடுத்துக்காட்டுகள், சமூகம்.</p><span class="go">etamil.in →</span></a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">உதவும் வழிகள்</p><h2>நிரல் எழுதத் தேவையில்லை</h2>
    <div class="grid">
      <div class="card"><h3>உங்கள் கைபேசியில் சோதியுங்கள்</h3><p>எந்தச் சாதனங்களிலும் ஆண்ட்ராய்டு பதிப்புகளிலும் இயங்குகிறது, எவற்றில் இயங்கவில்லை என்று சொல்லுங்கள். ஒவ்வொரு மாதிரியும் உதவும்.</p></div>
      <div class="card"><h3>மொழிபெயருங்கள்</h3><p>qos-இன் திரைகளையும் இந்த இணையதளத்தையும் தெளிவான, இயல்பான தமிழில் கொண்டுவர உதவுங்கள்.</p></div>
      <div class="card"><h3>கற்பியுங்கள்</h3><p>வகுப்பறைகளுக்கும் தாமாகக் கற்பவர்களுக்கும், கைபேசியில் இயங்கும் பாடங்களையும் பயிற்சிகளையும் பகிருங்கள்.</p></div>
    </div>
  </div>
</section>
"""

ABOUT = """
<header class="page-hero"><div class="wrap"><p class="eyebrow">பற்றி</p><h1>qos பற்றி</h1><p>qos — தமிழ் OS. இ-தமிழ் எழுத்துப்பெயர்ப்பில் த என்பது q.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="grid two">
      <div class="card"><h3>ஏன் qos</h3><p>கணினி வைத்திருப்பவர்களை விடப் பல மடங்கு மக்களிடம் ஆண்ட்ராய்டு கைபேசி உள்ளது. அந்தக் கைபேசியை qos உண்மையான நிரலாக்கக் கணினியாக மாற்றுகிறது; அதனால் மடிக்கணினி வாங்காமலேயே, தமிழிலோ ஆங்கிலத்திலோ, எவரும் நிரலாக்கம் கற்று மென்பொருள் கட்டலாம்.</p></div>
      <div class="card"><h3>திறந்த மூலத்தின் மேல் கட்டப்பட்டது</h3><p>qos, <a href="https://termux.dev">Termux</a>-ஐயும், qos Desktop, <a href="https://github.com/termux/termux-x11">Termux:X11</a>-ஐயும் அடிப்படையாகக் கொண்டவை; இரண்டும் GPLv3. உள்ளே உள்ள கருவிகள் Termux தொகுப்புத் திரட்டுகளிலிருந்து வருகின்றன. அவற்றை உருவாக்கும் அனைவருக்கும் நன்றி.</p></div>
      <div class="card"><h3>தனியுரிமை</h3><p>qos-இல் பகுப்பாய்வோ தொலைஅளவீடோ இல்லை; கணக்கும் தேவையில்லை. இந்த இணையதளம் குக்கீகளை அமைப்பதில்லை, பிற தளங்களிலிருந்து எதையும் ஏற்றுவதில்லை.</p></div>
      <div class="card"><h3>உரிமம்</h3><p>qos-உம் qos Desktop-உம் GNU General Public License v3 உரிமத்தின் கீழ் கட்டற்ற மென்பொருள். மூல நிரல் GitHub-இல்: <a href="https://github.com/Maruff/qos">qos</a>, <a href="https://github.com/Maruff/qos-desktop">qos Desktop</a>, <a href="https://github.com/Maruff/qos.ae">இந்த இணையதளம்</a>.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="brand">
  <div class="wrap">
    <p class="eyebrow">அடையாளம்</p><h2>சின்னமும் நிறங்களும்</h2>
    <p class="intro">qos-ஐச் சுட்டிக்காட்ட qos சின்னத்தைப் பயன்படுத்துங்கள். கருப்புப் பின்னணியிலேயே வைத்திருங்கள்; அதன் வடிவங்களையோ நிறங்களையோ மாற்றாதீர்கள்.</p>
    <div class="grid">
      <div class="card"><img src="@R@assets/qos-wordmark.png" alt="qos — தமிழ் OS" width="796" height="529" style="max-width:260px"><p style="margin-top:10px"><a href="@R@assets/qos-logo.png">முழுச் சின்னம் (PNG)</a></p></div>
      <div class="card"><img src="@R@assets/qos-icon-512.png" alt="qos சின்னம்" width="512" height="512" style="max-width:120px;border-radius:24px"><p style="margin-top:10px"><a href="@R@assets/qos-icon-512.png">செயலிச் சின்னம் (PNG)</a></p></div>
      <div class="card"><h3>நிறங்கள்</h3><p><span class="chip on">#10F3BE</span> qos பச்சைநீலம்<br><br><span class="chip">#000000</span> கருப்பு</p></div>
    </div>
  </div>
</section>
"""

TA = {
    "brand_title": "qos — உங்கள் கைபேசியில் ஒரு நிரலாக்கக் கணினி",
    "banner": "<strong>qos 0.2</strong> வெளியானது: qos Desktop உங்கள் கைபேசிக்கு லினக்ஸ் மேசைத்தளத்தைக் கொண்டுவருகிறது →",
    "menu": {"features/": "வசதிகள்", "download/": "பதிவிறக்கம்", "docs/": "ஆவணங்கள்", "roadmap/": "திட்டப் பாதை", "community/": "சமூகம்", "about/": "பற்றி"},
    "get": "qos பெறுக",
    "menu_button": "பட்டி",
    "other_language": "English",
    "footer_about": "qos ஆண்ட்ராய்டு கைபேசியையோ டேப்லெட்டையோ நிரலாக்கக் கணினியாக மாற்றுகிறது. GNU GPL v3 உரிமத்தின் கீழ் கட்டற்ற மென்பொருள்.",
    "legal": "qos — தமிழ் OS · Termux-ஐ அடிப்படையாகக் கொண்டது",
    "footer": [
        ("qos பெறுக", [("பதிவிறக்கம்", "@L@download/"), ("F-Droid களஞ்சியம்", "@L@download/#verify"), ("GitHub வெளியீடுகள்", "https://github.com/Maruff/qos/releases"), ("தேவைகள்", "@L@download/#requirements")]),
        ("கற்க", [("வசதிகள்", "@L@features/"), ("ஆவணங்கள்", "@L@docs/"), ("திட்டப் பாதை", "@L@roadmap/"), ("கேள்விகள்", "@L@docs/#faq")]),
        ("சமூகம்", [("மன்றம்", "https://github.com/Maruff/qos/discussions"), ("சிக்கலைத் தெரிவிக்க", "https://github.com/Maruff/qos/issues"), ("பங்களிக்க", "@L@community/"), ("இ-தமிழ்", "https://etamil.in/ta/")]),
        ("திட்டம்", [("பற்றி", "@L@about/"), ("qos மூல நிரல்", "https://github.com/Maruff/qos"), ("qos Desktop மூல நிரல்", "https://github.com/Maruff/qos-desktop"), ("அடையாளம்", "@L@about/#brand")]),
    ],
    "pages": {
        "": {"title": "முகப்பு", "description": "qos உங்கள் ஆண்ட்ராய்டு கைபேசியையோ டேப்லெட்டையோ நிரலாக்கக் கணினியாக மாற்றுகிறது: லினக்ஸ் முனையம், VS Code, தொகுப்பிகள், மேசைத்தளம், இ-தமிழ். இலவசம், திறந்த மூலம், கணக்கு தேவையில்லை.", "body": HOME},
        "features/": {"title": "வசதிகள்", "description": "qos என்ன செய்யும்: லினக்ஸ் முனையம், தொகுப்பிகள், VS Code, XFCE மேசைத்தளம், இ-தமிழ்; செயலிகள், விளையாட்டுகள், அசைவூட்டம், திரைப்படம், IoT, பாதுகாப்பு, AI.", "body": FEATURES},
        "download/": {"title": "பதிவிறக்கம்", "description": "qos-ஐ அதன் F-Droid களஞ்சியம், GitHub வெளியீடுகள் அல்லது Obtainium வழியாக நிறுவுங்கள்; நிறுவுவதைச் சரிபாருங்கள்.", "body": DOWNLOAD},
        "docs/": {"title": "ஆவணங்கள்", "description": "qos-ஐப் பயன்படுத்துவது எப்படி: முதல் முறை, முனையம், VS Code, qos Desktop, இ-தமிழ், பணி நிற்காமல் இருக்க, சிக்கல் தீர்வு.", "body": DOCS},
        "roadmap/": {"title": "திட்டப் பாதை", "description": "இன்று qos-இல் என்ன உள்ளது, அடுத்து என்ன வருகிறது, வெளியீட்டுக் குறிப்புகள்.", "body": ROADMAP},
        "community/": {"title": "சமூகம்", "description": "qos மன்றம், சிக்கல் பதிவேடு, பங்களிக்கும் வழிகள்.", "body": COMMUNITY},
        "about/": {"title": "பற்றி", "description": "qos ஏன், எதன் மேல் கட்டப்பட்டது, தனியுரிமை, உரிமம், அடையாளம்.", "body": ABOUT},
    },
}
