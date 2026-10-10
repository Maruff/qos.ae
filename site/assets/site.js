// qos.ae — shared behaviour for every page.
(function () {
  // The menu button on narrow screens.
  var nav = document.querySelector(".nav");
  var toggle = document.querySelector(".menu-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Show the F-Droid repository address the site is actually served from:
  // qos.ae, or GitHub Pages until the domain points here.
  var fingerprint = "6A57FBAEAE589E8B7D1BC7F2758A9E747A6CF66A22603A1718E16F390E944AB8";
  var root = new URL(document.documentElement.getAttribute("data-root") || "./", location.href);
  if (root.protocol !== "https:") return;
  var repo = root.href + "fdroid/repo";
  document.querySelectorAll("[data-fdroid-url]").forEach(function (el) { el.textContent = repo; });
  document.querySelectorAll("[data-fdroid-link]").forEach(function (el) {
    el.href = repo.replace(/^https:/, "fdroidrepos:") + "?fingerprint=" + fingerprint;
  });
})();
