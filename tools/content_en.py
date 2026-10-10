"""English text for qos.ae. See build.py for the @R@ / @L@ / @FP@ tokens."""

FIG = '<img class="{cls}" src="@R@assets/img/{name}.svg" alt="{alt}" width="{w}" height="{h}" loading="lazy"><p class="caption">Illustration</p>'


def fig(name, alt, tablet=False):
    w, h, cls = (960, 640, "tablet") if tablet else (360, 720, "phone")
    return '<div>' + FIG.format(cls=cls, name=name, alt=alt, w=w, h=h) + '</div>'


BEYOND = [
    ("apps", "Mobile apps",
     "Build Android apps from the terminal: Java 21, Kotlin, Gradle, aapt2, d8, apksigner and adb are all in the package collection. Web apps work fully.",
     "An Android kit set up in one step, and a starter project that builds and installs on the same phone with one command.",
     "Builds are slower than on a laptop. Flutter does not run on Android devices yet."),
    ("games", "Games",
     "Web games in HTML5 and JavaScript, and text games in any language. With qos Desktop: Godot 4, LÖVE, pygame and raylib.",
     "A game kit set up in one step, with starter projects.",
     "2D and light 3D. Phones lack the desktop graphics drivers that heavy 3D games need."),
    ("animation", "Cartoons and animation",
     "Animated explainers with manim, and image work with ImageMagick. With qos Desktop: frame-by-frame animation in Krita, and drawing in Inkscape and GIMP.",
     "A creative kit with these tools set up in one step.",
     "No Blender, so no 3D animation. Long renders are slow and warm the phone."),
    ("film", "Films",
     "Edit with ffmpeg: trim, join, add music and Tamil subtitles, and export for YouTube or WhatsApp. With qos Desktop: Kdenlive, Shotcut and Audacity.",
     "A film kit with editing, sound and subtitle tools set up in one step.",
     "Shoot with the phone's own camera app; qos edits the footage. Rendering 4K video is slow."),
    ("iot", "IoT",
     "MQTT with Mosquitto, Python and Node.js services, and talking to ESP32 or Arduino boards over Wi-Fi.",
     "An IoT kit: an MQTT broker, dashboards and over-the-air updates for ESP32 boards.",
     "Flashing boards over USB without root is hard on Android. We are exploring it, with eTamil on Arduino from the phone."),
    ("security", "Cybersecurity",
     "Scan your own network with nmap, encrypt with GnuPG and age, run WireGuard and Tor, scan files with ClamAV and YARA, and take apart programs and Android apps with radare2, gdb, apktool and jadx.",
     "A security kit for learning and defence, with practice exercises, and Wireshark on qos Desktop.",
     "Capturing network traffic and Wi-Fi monitoring need root. Attack frameworks are not included."),
    ("ai", "AI",
     "Run open-weight language models on the phone with llama.cpp or Ollama, and machine learning with PyTorch, ONNX Runtime, NumPy and SciPy. No account and no paid AI service.",
     "A local AI kit: a chosen model downloaded and ready, and a code assistant in VS Code that runs on the device.",
     "Small models only: about 1 to 4 billion parameters, needing roughly 4 to 8 GB of RAM. Answers are slower than cloud services."),
]


def beyond_rows():
    return "\n".join(
        f'<div class="cap-row" id="{key}"><h3>{name}</h3>'
        f'<div class="today"><span class="label">Today</span><p>{today}</p></div>'
        f'<div class="coming"><span class="label">Coming</span><p>{coming}</p></div>'
        f'<div class="limits"><span class="label">Limits</span><p>{limits}</p></div></div>'
        for key, name, today, coming, limits in BEYOND
    )


def beyond_tiles():
    return "\n".join(f'<a class="tile" href="@L@features/#{key}">{name}</a>' for key, name, *_ in BEYOND)


AUDIENCE = """
<div class="grid">
  <div class="card"><h3>Students</h3><p>Learn Python, C, Java or Rust on the device you already carry, without waiting for a computer lab.</p></div>
  <div class="card"><h3>Tamil speakers learning to code</h3><p>Write programs in Tamil with eTamil, and move on to other languages from the same terminal.</p></div>
  <div class="card"><h3>Teachers and colleges</h3><p>Run programming classes on phones and tablets. Every student gets the same tools, set up the same way.</p></div>
  <div class="card"><h3>Working developers</h3><p>Fix a bug, review a branch, push a commit or reach a server over SSH, away from your desk.</p></div>
  <div class="card"><h3>eTamil developers</h3><p>Build and test eTamil programs, modules and servers on Android, with the real compiler.</p></div>
  <div class="card"><h3>Makers and tinkerers</h3><p>Automate your phone, run small servers, talk to boards over Wi-Fi and explore Linux, safely, inside one app.</p></div>
</div>"""

REQUIREMENTS = """
<table class="table">
  <thead><tr><th></th><th>Minimum</th><th>Recommended</th></tr></thead>
  <tbody>
    <tr><th>Android</th><td class="strong" data-label="Minimum">7.0 (Nougat)</td><td data-label="Recommended">10 or newer</td></tr>
    <tr><th>Processor</th><td class="strong" data-label="Minimum">ARM (32 or 64-bit) or x86</td><td data-label="Recommended">64-bit ARM (arm64-v8a), which almost every phone since 2017 has. The eTamil toolchain needs it.</td></tr>
    <tr><th>Memory (RAM)</th><td class="strong" data-label="Minimum">3 GB</td><td data-label="Recommended">4 GB or more for VS Code, Rust builds and qos Desktop; 6 to 8 GB for local AI models</td></tr>
    <tr><th>Free storage</th><td class="strong" data-label="Minimum">4 GB</td><td data-label="Recommended">8 GB or more. The developer toolset takes about 2.3 GB once installed, and qos Desktop's XFCE about 0.6 GB more.</td></tr>
    <tr><th>Internet</th><td class="strong" data-label="Minimum">For the first launch: about 500 MB</td><td data-label="Recommended">Wi-Fi for setup. After that, qos works offline.</td></tr>
    <tr><th>Input</th><td class="strong" data-label="Minimum">The on-screen keyboard</td><td data-label="Recommended">A Bluetooth or USB keyboard, especially on a tablet; a mouse for qos Desktop</td></tr>
  </tbody>
</table>
<p class="small">Storage and download sizes are measured from the current package versions and change as they update. Memory figures are guidance, not hard limits.</p>"""

STAGES = """
<div class="roadmap">
  <div class="stage"><span class="tag">Available now · v0.2</span><h3>A working development machine</h3><ul>
    <li>Linux terminal with the full Termux package collection</li>
    <li>One-time setup of git, clang, make, Python, Rust and Java 17</li>
    <li>VS Code inside the app, signed in automatically</li>
    <li>qos Desktop: an XFCE desktop for graphical apps <span class="new">New</span></li>
    <li>eTamil compiler and its library, nUlakam (64-bit ARM)</li>
    <li>Signed releases on GitHub and the qos F-Droid repository</li></ul></div>
  <div class="stage"><span class="tag amber">Next</span><h3>Smoother everyday use</h3><ul>
    <li>eTamil built natively for Android, so eTamil programs can reach websites and APIs by name</li>
    <li>Choose which tools to install at first launch</li>
    <li>The app's own screens in Tamil</li>
    <li>VS Code settings: start on launch, choose the port</li></ul></div>
  <div class="stage"><span class="tag violet">Planned</span><h3>Kits for every kind of work</h3><ul>
    <li><strong>Setup by purpose:</strong> choose what you are here to do at first launch, and qos installs the matching kit</li>
    <li>Kits for Android apps, games, animation, film, IoT, security and local AI</li>
    <li>qos add-ons for the device: notifications, sensors, camera, widgets and start-on-boot scripts</li>
    <li>A full Debian environment for tools Termux does not package</li></ul></div>
  <div class="stage"><span class="tag grey">Exploring</span><h3>Ideas we are looking into</h3><ul>
    <li>qos Desktop built into qos itself: one app instead of two</li>
    <li>Flashing boards over USB without root, and eTamil on Arduino from the phone</li>
    <li>Ready-made lessons for classrooms</li>
    <li>Documentation in Tamil and English</li></ul></div>
</div>"""

FDROID_STEPS = """
<ol>
  <li>Install an F-Droid client: <a href="https://f-droid.org">F-Droid</a>, Droid-ify or Neo Store.</li>
  <li>On your phone, tap <a data-fdroid-link href="fdroidrepos://qos.ae/fdroid/repo?fingerprint=@FP@">Add the qos repository</a>, or add it by hand:
    <span class="url" data-fdroid-url>https://qos.ae/fdroid/repo</span>and check this fingerprint:<span class="url">@FP@</span></li>
  <li>Search for <strong>qos</strong> and install it. Add <strong>qos Desktop</strong> too if you want the desktop.</li>
</ol>"""

HOME = f"""
<header class="hero">
  <div class="wrap">
    <div>
      <p class="eyebrow">Free and open source · Android 7 and newer</p>
      <h1>Your phone is a development machine.</h1>
      <p class="sub">qos puts a Linux terminal, VS Code, compilers, a desktop and the eTamil toolchain on your Android phone or tablet. Write, build and run real software anywhere, with no laptop and no account.</p>
      <div class="cta"><a class="btn primary" href="@L@download/">Get qos</a><a class="btn ghost" href="@L@features/">See what's inside</a></div>
      <div class="facts"><span>GPLv3</span><span>No account, no ads, no tracking</span><span>Works offline after setup</span><span>No root needed</span></div>
    </div>
    <div class="art">{FIG.format(cls="phone", name="phone-terminal", alt="qos terminal on a phone", w=360, h=720)}</div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="feature flip">
      <div class="media">{fig("tablet-vscode", "VS Code running inside qos on a tablet", True)}</div>
      <div><p class="eyebrow">Editor</p><h2>VS Code, inside the app</h2>
        <p>A full VS Code runs on the device and opens from the side drawer: the file tree, extensions from Open VSX, and a terminal underneath. No cloud and no sign-in; your code never leaves the phone unless you push it.</p>
        <p class="note">Best on a tablet with a keyboard. On a phone, the terminal and a text editor are often quicker.</p>
        <a class="more" href="@L@docs/#vscode">How VS Code works in qos →</a></div>
    </div>
    <div class="feature">
      <div class="media">{fig("tablet-desktop", "The XFCE desktop in qos Desktop on a tablet", True)}</div>
      <div><p class="eyebrow">Desktop <span class="new">New in 0.2</span></p><h2>A Linux desktop when you need one</h2>
        <p>Tap Desktop in the drawer and qos opens XFCE on qos Desktop, its companion display. Run graphical tools: Krita and Inkscape for drawing and animation, Kdenlive for video, Godot for games, Wireshark for networks.</p>
        <p class="note">qos Desktop is a second app from the same source, signed with the same key, and runs as part of qos. The first start downloads about 100 MB.</p>
        <a class="more" href="@L@docs/#desktop">Start the desktop →</a></div>
    </div>
    <div class="feature flip">
      <div class="media">{fig("phone-etamil", "An eTamil program in Tamil and its output")}</div>
      <div><p class="eyebrow">eTamil</p><h2>Write code in Tamil</h2>
        <p>qos comes with eTamil, a programming language written in Tamil, and its standard library. Learn to program in your own language, then use the same terminal for Python, C or Rust.</p>
        <a class="more" href="https://etamil.in">Learn eTamil at etamil.in →</a></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">What's inside</p><h2>The tools you would install on a laptop</h2>
    <p class="intro">Set up on first launch, or one <code>pkg install</code> away from a collection of thousands of packages.</p>
    <div class="chip-group"><h3>Installed at first launch</h3><div class="chips">
      <span class="chip on">git</span><span class="chip on">clang / C / C++</span><span class="chip on">make</span><span class="chip on">Python</span><span class="chip on">Rust</span><span class="chip on">Java 17</span><span class="chip on">Node.js</span><span class="chip on">VS Code (code-server)</span><span class="chip on">eTamil</span><span class="chip on">nUlakam</span></div></div>
    <div class="chip-group"><h3>One command away</h3><div class="chips">
      <span class="chip">Kotlin</span><span class="chip">Gradle</span><span class="chip">Go</span><span class="chip">PHP</span><span class="chip">Ruby</span><span class="chip">PostgreSQL</span><span class="chip">SQLite</span><span class="chip">Redis</span><span class="chip">nginx</span><span class="chip">OpenSSH</span><span class="chip">neovim</span><span class="chip">ffmpeg</span><span class="chip">nmap</span><span class="chip">llama.cpp</span><span class="chip">XFCE</span><span class="chip">Krita</span><span class="chip">Godot</span></div></div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Who it's for</p><h2>For anyone with a phone and something to build</h2>
    <p class="intro">Most people who want to learn programming already own an Android phone. Far fewer own a laptop. qos is for them, and for anyone who wants their tools within reach.</p>
    {AUDIENCE}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">Beyond code</p><h2>Apps, games, cartoons, films, IoT, security and AI</h2>
    <p class="intro">qos is more than a code editor. See what each kind of work looks like today, and what the roadmap adds.</p>
    <div class="tiles">{beyond_tiles()}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Trust</p><h2>Open, private and verifiable</h2>
    <div class="grid four">
      <div class="card"><h3>Open source</h3><p>Every line is public under the GNU GPL v3, built on Termux and Termux:X11.</p></div>
      <div class="card"><h3>No account</h3><p>No sign-in, no ads, no analytics, no telemetry. This website sets no cookies.</p></div>
      <div class="card"><h3>Signed releases</h3><p>Every APK is signed with the qos key, and the F-Droid repository with its own; both fingerprints are published.</p></div>
      <div class="card"><h3>Built in the open</h3><p>Releases are built by public GitHub workflows from tagged source, with SHA-256 checksums.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">Get started</p><h2>Three steps</h2>
    <div class="steps">
      <div class="card step"><h3>Add the qos repository</h3><p>In F-Droid, add the qos repository and check its fingerprint. Or download the APK from GitHub.</p></div>
      <div class="card step"><h3>Install and open qos</h3><p>On first launch qos sets up its tools. Use Wi-Fi: it downloads about 500 MB.</p></div>
      <div class="card step"><h3>Start building</h3><p>Type in the terminal, or swipe in from the left for VS Code and Desktop.</p></div>
    </div>
    <p style="margin-top:24px"><a class="btn primary" href="@L@download/">Go to Download</a></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="band"><div><h2>Where qos is going</h2><p>Small releases every month: kits for every kind of work, and setup by purpose.</p></div><a class="btn ghost" href="@L@roadmap/">See the roadmap</a></div>
  </div>
</section>
"""

FEATURES = f"""
<header class="page-hero"><div class="wrap"><p class="eyebrow">Features</p><h1>Everything a development machine needs</h1><p>A Linux terminal, real compilers, VS Code, a desktop and eTamil, in one app on your phone or tablet.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="feature">
      <div class="media">{fig("phone-terminal", "qos terminal on a phone")}</div>
      <div><p class="eyebrow">Terminal</p><h2>A real Linux terminal</h2>
        <p>qos is built on Termux, so the whole Termux package collection works: thousands of packages, installed with <code>pkg install</code>. A row of extra keys gives you Esc, Ctrl, Tab and the arrows on a touch screen.</p>
        <p>git, clang, make, Python, Rust and Java 17 are set up the first time qos opens, along with VS Code and eTamil.</p></div>
    </div>
    <div class="feature flip">
      <div class="media">{fig("tablet-vscode", "VS Code running inside qos on a tablet", True)}</div>
      <div><p class="eyebrow">Editor</p><h2>VS Code, inside the app</h2>
        <p>code-server runs on the device and opens from the side drawer. qos signs you in with code-server's own password, and keeps that password on, because every app on the phone can reach the port it listens on.</p>
        <p>Extensions come from Open VSX, the open extension registry.</p></div>
    </div>
    <div class="feature">
      <div class="media">{fig("tablet-desktop", "The XFCE desktop in qos Desktop on a tablet", True)}</div>
      <div><p class="eyebrow">Desktop <span class="new">New in 0.2</span></p><h2>qos Desktop</h2>
        <p>An XFCE desktop on qos Desktop, the companion display built from Termux:X11. It runs as part of qos, so Android treats the two as one app. Use it for anything with windows: Krita, Inkscape, GIMP, Kdenlive, Shotcut, Audacity, Godot, Wireshark and Firefox.</p>
        <p class="note">Phones have no desktop graphics drivers, so heavy 3D is slow. A mouse or a keyboard with a touchpad helps.</p></div>
    </div>
    <div class="feature flip">
      <div class="media">{fig("phone-etamil", "An eTamil program in Tamil and its output")}</div>
      <div><p class="eyebrow">eTamil</p><h2>Programming in Tamil</h2>
        <p>The eTamil compiler and its standard library, nUlakam, are installed at first launch. eTamil programs read files, use SQLite, call web APIs and run servers.</p>
        <p class="note">qos currently ships eTamil's general Linux build, in which looking up internet addresses by name may not work on Android. A native Android build is next on the roadmap.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="beyond">
  <div class="wrap">
    <p class="eyebrow">Beyond code</p><h2>Apps, games, cartoons, films, IoT, security and AI</h2>
    <p class="intro">What each kind of work looks like in qos today, what the roadmap adds, and the honest limits, based on what the package collections actually carry.</p>
    <div class="cap">{beyond_rows()}</div>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Who it's for</p><h2>Built for learners and makers</h2>
    {AUDIENCE}
  </div>
</section>
"""

DOWNLOAD = f"""
<header class="page-hero"><div class="wrap"><p class="eyebrow">Download</p><h1>Get qos</h1><p>qos is free. Choose how to install it; F-Droid is recommended because updates then arrive by themselves.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="grid">
      <div class="card recommended"><span class="tag">Recommended</span><h3>F-Droid repository</h3><p>Add the qos repository to an F-Droid client once.</p>
        <ul class="pros"><li class="plus">Automatic updates for qos and qos Desktop</li><li class="plus">Signed index, checked against a fingerprint</li><li class="minus">Needs an F-Droid client</li></ul>
        {FDROID_STEPS}</div>
      <div class="card"><span class="tag grey">Direct</span><h3>GitHub releases</h3><p>Download the APK and install it yourself.</p>
        <ul class="pros"><li class="plus">No extra app</li><li class="plus">SHA-256 checksums with every release</li><li class="minus">Update by hand</li></ul>
        <ol><li>Open the <a href="https://github.com/Maruff/qos/releases/latest">latest qos release</a>.</li><li>Download the APK for your phone (see below).</li><li>Open it, and allow your browser to install apps when Android asks.</li></ol></div>
      <div class="card"><span class="tag grey">Updater</span><h3>Obtainium</h3><p>Let Obtainium follow the GitHub releases.</p>
        <ul class="pros"><li class="plus">Updates from GitHub, without F-Droid</li><li class="minus">One more app to set up</li></ul>
        <ol><li>Install <a href="https://github.com/ImranR98/Obtainium">Obtainium</a>.</li><li>Add <code>https://github.com/Maruff/qos</code> as an app source.</li></ol></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">Which APK</p><h2>Pick the APK for your processor</h2>
    <p class="intro">F-Droid picks for you. From GitHub, choose by your phone's processor; if you are not sure, it is almost certainly arm64-v8a.</p>
    <table class="table"><thead><tr><th>File</th><th>For</th></tr></thead><tbody>
      <tr><th><code>qos-…-arm64-v8a.apk</code></th><td data-label="For">Almost every phone and tablet since 2017. Recommended.</td></tr>
      <tr><th><code>qos-…-armeabi-v7a.apk</code></th><td data-label="For">Older and low-cost 32-bit phones. No eTamil toolchain yet.</td></tr>
      <tr><th><code>qos-…-x86_64.apk</code></th><td data-label="For">Chromebooks and Android emulators.</td></tr>
      <tr><th><code>qos-…-x86.apk</code></th><td data-label="For">Old 32-bit Intel devices.</td></tr>
    </tbody></table>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="feature">
      <div class="media">{fig("tablet-desktop", "The XFCE desktop in qos Desktop", True)}</div>
      <div><p class="eyebrow">Add-on</p><h2>qos Desktop</h2>
        <p>Want windows and a mouse pointer? Install qos Desktop after qos: from the same F-Droid repository, or <a href="https://github.com/Maruff/qos-desktop/releases/latest">qos-desktop.apk</a> from GitHub. Then tap Desktop in the qos side drawer.</p>
        <p class="note">qos Desktop only works with qos from these same sources, because both must be signed with the qos key.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="verify">
  <div class="wrap">
    <p class="eyebrow">Verify</p><h2>Check what you install</h2>
    <p class="intro">Every release lists SHA-256 checksums in <code>sha256sums.txt</code>. These are the certificates that sign qos:</p>
    <table class="table"><tbody>
      <tr><th>qos and qos Desktop APKs</th><td><code>379DA39A198B76D7AE4733C8FC78648CB509D2C1174D03E64442C9337FDEF8DA</code></td></tr>
      <tr><th>qos F-Droid repository</th><td><code>@FP@</code></td></tr>
    </tbody></table>
    <p class="small">With the Android SDK: <code>apksigner verify --print-certs qos-….apk</code> shows the APK's SHA-256 certificate digest.</p>
  </div>
</section>

<section id="requirements">
  <div class="wrap">
    <p class="eyebrow">Requirements</p><h2>What your device needs</h2>
    {REQUIREMENTS}
    <div class="notes">
      <div class="note"><strong>qos replaces Termux.</strong> It uses Termux's package name so that every Termux package works, so the two cannot be installed side by side, and Termux add-ons will not work with qos. Back up anything you need from Termux first.</div>
      <div class="note"><strong>Not on Google Play.</strong> Play does not allow apps that run programs they download, which is what a development machine does.</div>
    </div>
  </div>
</section>
"""

DOCS = """
<header class="page-hero"><div class="wrap"><p class="eyebrow">Docs</p><h1>Using qos</h1><p>From first launch to the desktop, and what to do when something goes wrong.</p></div></header>

<section class="flush">
  <div class="wrap docs">
    <nav class="toc" aria-label="On this page">
      <a href="#first-launch">First launch</a><a href="#terminal">The terminal</a><a href="#storage">Your files</a><a href="#vscode">VS Code</a><a href="#desktop">qos Desktop</a><a href="#etamil">eTamil</a><a href="#background">Keeping work running</a><a href="#updates">Updates</a><a href="#troubleshooting">Troubleshooting</a><a href="#faq">Questions</a>
    </nav>
    <div class="doc">
      <section id="first-launch"><h2>First launch</h2>
        <p>The first time qos opens, it installs its base system and then runs <code>qos-setup</code>, which installs git, clang, make, Python, Rust, Java 17, code-server and eTamil. It downloads about 500 MB, so use Wi-Fi and keep the screen on. You will see <strong>Done</strong> in the terminal when it finishes.</p>
        <p>If setup is interrupted, it carries on at the next start. You can also run it again at any time:</p><pre>qos-setup</pre></section>
      <section id="terminal"><h2>The terminal</h2>
        <p>Install anything from the package collection with <code>pkg</code>:</p><pre>pkg search postgres
pkg install postgresql</pre>
        <p>Swipe in from the left edge for the drawer: sessions, the keyboard toggle, VS Code and Desktop. Long-press the keyboard button to show or hide the extra keys row.</p></section>
      <section id="storage"><h2>Your files</h2>
        <p>Your projects live in qos's home folder. To reach the phone's shared storage (Downloads, Pictures, camera footage), run once:</p><pre>termux-setup-storage</pre><p>It asks for permission and creates <code>~/storage</code> with links to those folders.</p></section>
      <section id="vscode"><h2>VS Code</h2>
        <p>Tap <strong>VS Code</strong> in the drawer. qos starts code-server in the background if it is not already running, and signs you in with the password from <code>~/.config/code-server/config.yaml</code>.</p>
        <p>The password stays on deliberately: every app on the phone can reach 127.0.0.1:8080, and code-server can run commands. To start it yourself: <code>code-server</code>.</p></section>
      <section id="desktop"><h2>qos Desktop</h2>
        <p>Install qos Desktop from the qos F-Droid repository, then tap <strong>Desktop</strong> in the drawer. The first time, qos installs XFCE (about 100 MB) and the <code>qos-x11</code> package, then opens the desktop. From a terminal: <code>qos-desktop</code>.</p>
        <p>Stop it by logging out of XFCE, with Exit in the qos Desktop notification, or with Ctrl+C in the session that started it. Graphical programs started from a terminal need <code>DISPLAY=:1</code>.</p>
        <p>If the screen stays black or colours look swapped, start it by hand with an option:</p><pre>termux-x11 :1 -legacy-drawing -xstartup "xfce4-session"
termux-x11 :1 -force-bgra -xstartup "xfce4-session"</pre></section>
      <section id="etamil"><h2>eTamil</h2>
        <p>Run an eTamil program with the virtual machine, and check one without running it:</p><pre>etamil --vm program.qmz
etamil --check program.qmz</pre>
        <p>The standard library is in <code>$ETAMIL_PATH</code>, so <code>இறக்கு "nUlakam/…"</code> works from any folder. Learn the language at <a href="https://etamil.in">etamil.in</a>.</p></section>
      <section id="background"><h2>Keeping work running</h2>
        <p>Android 12 and newer may stop long-running work in the background, such as builds, VS Code or the desktop. On Android 14 and later, turn on Developer options and enable <strong>Disable child process restrictions</strong>. Setting qos's battery use to <strong>Unrestricted</strong> also helps.</p></section>
      <section id="updates"><h2>Updates</h2>
        <p>With the F-Droid repository, qos and qos Desktop update like any other app. Packages inside qos update with:</p><pre>pkg upgrade</pre></section>
      <section id="troubleshooting"><h2>Troubleshooting</h2>
        <details><summary>Setup stopped with an error</summary><p>Check the internet connection and run <code>qos-setup</code> again. Each step is safe to repeat.</p></details>
        <details><summary>"qos Desktop is not installed"</summary><p>Install qos Desktop from the qos F-Droid repository or the qos-desktop GitHub release, then tap Desktop again.</p></details>
        <details><summary>"Signature verification … failed"</summary><p>qos Desktop and the qos-x11 package come from different sources. Install both from qos releases, not from Termux.</p></details>
        <details><summary>VS Code does not open</summary><p>Run <code>code-server</code> in the terminal to see the error. If it is not installed, run <code>qos-setup</code>.</p></details>
      </section>
      <section id="faq"><h2>Questions</h2>
        <details><summary>Is qos free?</summary><p>Yes. qos is free software under the GNU GPL v3, with no ads, no in-app purchases and no account.</p></details>
        <details><summary>Does qos need root?</summary><p>No. Everything runs inside the app's own storage, with normal app permissions.</p></details>
        <details><summary>How is qos different from Termux?</summary><p>qos is built on Termux and keeps its package collection. It adds a one-time setup of a complete toolset, VS Code inside the app, qos Desktop and eTamil, so a new phone becomes a development machine without configuration.</p></details>
        <details><summary>Can I keep Termux installed?</summary><p>No. qos uses Termux's package name so that every Termux package works, and Android allows one app with that name.</p></details>
        <details><summary>Why is qos not on Google Play?</summary><p>Play requires apps to target recent Android versions, which do not let an app run programs it downloads. A development machine has to do exactly that.</p></details>
      </section>
    </div>
  </div>
</section>
"""

ROADMAP = f"""
<header class="page-hero"><div class="wrap"><p class="eyebrow">Roadmap</p><h1>Where qos is, and where it is going</h1><p>qos ships small releases every month. Anything not yet released can change, and what you say in the forum shapes the order.</p></div></header>

<section class="flush">
  <div class="wrap">{STAGES}</div>
</section>

<section class="alt" id="purpose">
  <div class="wrap">
    <p class="eyebrow">Planned</p><h2>Setup by purpose</h2>
    <p class="intro">When qos is mature, its first launch will ask what you are here to do, and install the kit for that work instead of everything.</p>
    <div class="tiles four">
      <span class="tile">Business apps<small>eTamil, Python, Node.js, PostgreSQL</small></span>
      <span class="tile">Mobile apps<small>Kotlin, Gradle, Android tools</small></span>
      <span class="tile">Games<small>Godot, LÖVE, pygame</small></span>
      <span class="tile">Cybersecurity<small>nmap, radare2, jadx</small></span>
      <span class="tile">AI<small>llama.cpp, PyTorch</small></span>
      <span class="tile">Film-making<small>ffmpeg, Kdenlive</small></span>
      <span class="tile">IoT<small>MQTT, ESP32</small></span>
      <span class="tile">Learning<small>Python, eTamil, lessons</small></span>
    </div>
  </div>
</section>

<section id="releases">
  <div class="wrap">
    <p class="eyebrow">Release notes</p><h2>What changed</h2>
    <div class="grid two">
      <div class="card"><span class="tag">11 October 2026</span><h3>qos 0.2 and qos Desktop 0.1</h3><ul>
        <li>A Desktop button in the drawer opens an XFCE desktop on qos Desktop, setting it up the first time.</li>
        <li>qos Desktop: the Termux:X11 display, signed with the qos key so it runs as part of qos.</li>
        <li>Both are in the qos F-Droid repository.</li></ul>
        <p style="margin-top:10px"><a href="https://github.com/Maruff/qos/releases/tag/v0.2.0">qos 0.2.0</a> · <a href="https://github.com/Maruff/qos-desktop/releases/tag/v0.1.0">qos Desktop 0.1.0</a></p></div>
      <div class="card"><span class="tag grey">10 October 2026</span><h3>qos 0.1</h3><ul>
        <li>The first release: Termux with a one-time setup of git, clang, Python, Rust, Java 17, code-server and eTamil.</li>
        <li>VS Code inside the app, with automatic sign-in.</li>
        <li>Signed APKs for four processor types, and the qos F-Droid repository.</li></ul>
        <p style="margin-top:10px"><a href="https://github.com/Maruff/qos/releases/tag/v0.1.0">qos 0.1.0</a></p></div>
    </div>
  </div>
</section>
"""

COMMUNITY = """
<header class="page-hero"><div class="wrap"><p class="eyebrow">Community</p><h1>Ask, share and help shape qos</h1><p>qos is built in the open. Questions, ideas and bug reports are all welcome, in English or Tamil.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="grid two">
      <a class="card link" href="https://github.com/Maruff/qos/discussions"><span class="tag">Forum</span><h3>Discussions</h3><p>Ask questions, show what you built with qos, and suggest what comes next.</p><span class="go">Open the forum →</span></a>
      <a class="card link" href="https://github.com/Maruff/qos/issues"><span class="tag amber">Issues</span><h3>Report a problem</h3><p>Something broken? Include your phone model, Android version and what you ran.</p><span class="go">Open an issue →</span></a>
      <a class="card link" href="https://github.com/Maruff/qos"><span class="tag violet">Code</span><h3>Contribute</h3><p>Pull requests, Tamil translations and testing on more devices all help. The code is GPLv3.</p><span class="go">qos on GitHub →</span></a>
      <a class="card link" href="https://etamil.in"><span class="tag grey">Language</span><h3>eTamil</h3><p>The Tamil programming language that ships with qos, with its guide, examples and community.</p><span class="go">etamil.in →</span></a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <p class="eyebrow">Ways to help</p><h2>No code needed</h2>
    <div class="grid">
      <div class="card"><h3>Test on your phone</h3><p>Tell us which devices and Android versions work, and which do not. Every model helps.</p></div>
      <div class="card"><h3>Translate</h3><p>Help put qos's screens and this website into clear, natural Tamil.</p></div>
      <div class="card"><h3>Teach</h3><p>Share lessons and exercises that work on a phone, for classrooms and for self-learners.</p></div>
    </div>
  </div>
</section>
"""

ABOUT = """
<header class="page-hero"><div class="wrap"><p class="eyebrow">About</p><h1>About qos</h1><p>qos — தமிழ் OS. q is how eTamil writes the Tamil letter த.</p></div></header>

<section class="flush">
  <div class="wrap">
    <div class="grid two">
      <div class="card"><h3>Why qos</h3><p>Far more people own an Android phone than a computer. qos turns that phone into a real development machine, so anyone can learn to program and build software, in Tamil or in English, without buying a laptop.</p></div>
      <div class="card"><h3>Built on open source</h3><p>qos is built on <a href="https://termux.dev">Termux</a>, and qos Desktop on <a href="https://github.com/termux/termux-x11">Termux:X11</a>, both GPLv3. The tools inside come from the Termux package collections. Thank you to everyone who makes them.</p></div>
      <div class="card"><h3>Privacy</h3><p>qos has no analytics and no telemetry, and needs no account. This website sets no cookies and loads nothing from other sites.</p></div>
      <div class="card"><h3>Licence</h3><p>qos and qos Desktop are free software under the GNU General Public License v3. The source is on GitHub: <a href="https://github.com/Maruff/qos">qos</a>, <a href="https://github.com/Maruff/qos-desktop">qos Desktop</a>, <a href="https://github.com/Maruff/qos.ae">this website</a>.</p></div>
    </div>
  </div>
</section>

<section class="alt" id="brand">
  <div class="wrap">
    <p class="eyebrow">Brand</p><h2>Logo and colours</h2>
    <p class="intro">Use the qos logo to point people to qos. Keep it on black, and do not change its shapes or colours.</p>
    <div class="grid">
      <div class="card"><img src="@R@assets/qos-wordmark.png" alt="qos — தமிழ் OS" width="796" height="529" style="max-width:260px"><p style="margin-top:10px"><a href="@R@assets/qos-logo.png">Full logo (PNG)</a></p></div>
      <div class="card"><img src="@R@assets/qos-icon-512.png" alt="qos icon" width="512" height="512" style="max-width:120px;border-radius:24px"><p style="margin-top:10px"><a href="@R@assets/qos-icon-512.png">App icon (PNG)</a></p></div>
      <div class="card"><h3>Colours</h3><p><span class="chip on">#10F3BE</span> qos teal<br><br><span class="chip">#000000</span> black</p></div>
    </div>
  </div>
</section>
"""

EN = {
    "brand_title": "qos — a development machine in your pocket",
    "banner": "<strong>qos 0.2</strong> is out: qos Desktop brings a Linux desktop to your phone →",
    "menu": {"features/": "Features", "download/": "Download", "docs/": "Docs", "roadmap/": "Roadmap", "community/": "Community", "about/": "About"},
    "get": "Get qos",
    "menu_button": "Menu",
    "other_language": "தமிழ்",
    "footer_about": "qos turns an Android phone or tablet into a development machine. Free software under the GNU GPL v3.",
    "legal": "qos — தமிழ் OS · built on Termux",
    "footer": [
        ("Get qos", [("Download", "@L@download/"), ("F-Droid repository", "@L@download/#verify"), ("GitHub releases", "https://github.com/Maruff/qos/releases"), ("Requirements", "@L@download/#requirements")]),
        ("Learn", [("Features", "@L@features/"), ("Docs", "@L@docs/"), ("Roadmap", "@L@roadmap/"), ("Questions", "@L@docs/#faq")]),
        ("Community", [("Forum", "https://github.com/Maruff/qos/discussions"), ("Report a problem", "https://github.com/Maruff/qos/issues"), ("Contribute", "@L@community/"), ("eTamil", "https://etamil.in")]),
        ("Project", [("About", "@L@about/"), ("qos source", "https://github.com/Maruff/qos"), ("qos Desktop source", "https://github.com/Maruff/qos-desktop"), ("Brand", "@L@about/#brand")]),
    ],
    "pages": {
        "": {"title": "Home", "description": "qos turns an Android phone or tablet into a development machine: a Linux terminal, VS Code, compilers, a desktop and the eTamil toolchain. Free, open source, no account.", "body": HOME},
        "features/": {"title": "Features", "description": "What qos can do: a Linux terminal, compilers, VS Code, an XFCE desktop and eTamil, plus apps, games, animation, film, IoT, security and AI.", "body": FEATURES},
        "download/": {"title": "Download", "description": "Install qos from its F-Droid repository, GitHub releases or Obtainium, and check what you install.", "body": DOWNLOAD},
        "docs/": {"title": "Docs", "description": "How to use qos: first launch, the terminal, VS Code, qos Desktop, eTamil, keeping work running and troubleshooting.", "body": DOCS},
        "roadmap/": {"title": "Roadmap", "description": "What is in qos today, what comes next, and release notes.", "body": ROADMAP},
        "community/": {"title": "Community", "description": "The qos forum, issue tracker and ways to contribute.", "body": COMMUNITY},
        "about/": {"title": "About", "description": "Why qos exists, what it is built on, privacy, licence and brand.", "body": ABOUT},
    },
}
