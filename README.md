# qos.ae

The website for [qos](https://github.com/Maruff/qos), and its F-Droid repository.

| Path | What |
| --- | --- |
| `index.html`, `assets/` | the site at qos.ae |
| `fdroid/config.yml`, `fdroid/metadata/` | the F-Droid repository, built from the signed APKs on the qos GitHub releases |
| `.github/workflows/publish.yml` | builds both and deploys them to GitHub Pages |

The F-Droid repository is served at `/fdroid/repo`. Its signing key's SHA-256
fingerprint, which people check when they add the repository, is:

```
6A57FBAEAE589E8B7D1BC7F2758A9E747A6CF66A22603A1718E16F390E944AB8
```

The key itself is never in this repository; the workflow reads it from the
`FDROID_KEYSTORE_BASE64` and `FDROID_KEYSTORE_PASSWORD` secrets.

## Pointing qos.ae here

Until the domain is set up the site is at <https://maruff.github.io/qos.ae/>.
To move it: point the domain's DNS at GitHub Pages, then set `qos.ae` as the
custom domain in the Pages settings. The F-Droid address follows the page
automatically on the next publish, and the old `github.io` address redirects.
