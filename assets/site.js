// Show the F-Droid repository address the site is actually served from:
// qos.ae, or GitHub Pages until the domain points here.
(function () {
  var fingerprint = "6A57FBAEAE589E8B7D1BC7F2758A9E747A6CF66A22603A1718E16F390E944AB8";
  var root = new URL(document.documentElement.getAttribute("data-root") || "./", location.href);
  if (root.protocol !== "https:") return;
  var repo = root.href + "fdroid/repo";
  document.querySelectorAll("[data-fdroid-url]").forEach(function (el) { el.textContent = repo; });
  document.querySelectorAll("[data-fdroid-link]").forEach(function (el) {
    el.href = repo.replace(/^https:/, "fdroidrepos:") + "?fingerprint=" + fingerprint;
  });
})();
