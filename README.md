# home-assistant-android-icon-map

Generates a variant of [MDI](https://materialdesignicons.com/)'s icon meta file. This includes IDs used by [icondialoglib](https://github.com/maltaisn/icondialoglib), which was previously used inside Home Assistant for Android.

- icondialoglib's ID mapping is fetched from GitHub. The fetched commit can be configured in `package.json`.
- Running `generator.js` will generate a new copy of `meta.json`.
