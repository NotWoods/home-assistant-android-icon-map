// @ts-check
import { getMeta, getVersion } from "@mdi/util";
import { readFile, writeFile } from "fs/promises";

/**
 * Loads user config from package.json.
 */
async function loadConfig() {
  const packageJsonFile = await readFile(
    new URL("./package.json", import.meta.url),
    "utf8"
  );
  /** @type {import ('./package.json')} Confirguration storing Git versions to load */
  const { config } = JSON.parse(packageJsonFile);
  return config;
}

/**
 * Fetches a map of icon character codes to numeric IDs.
 * The IDs are used by icondialoglib to identify icons.
 * @param {string} commit Git commit to fetch
 * @returns {Promise<Map<string, number>>}
 */
async function fetchIconDialogIdMapping(commit) {
  const res = await fetch(
    `https://raw.githubusercontent.com/maltaisn/icondialoglib/${commit}/utils/mdi_id_map.json`
  );
  /** @type {{ [charcode: string]: number }} */
  const map = await res.json();

  return new Map(
    Object.entries(map).map(([charcode, id]) => [charcode.toLowerCase(), id])
  );
}

const config = await loadConfig();
const dialogIdMap = await fetchIconDialogIdMapping(config.icondialoglib_commit);
const iconMeta = getMeta();

const mappedIconMeta = iconMeta.map((icon) => ({
  name: icon.name,
  codepoint: icon.codepoint,
  dialoglib_id: dialogIdMap.get(icon.codepoint.toLowerCase()),
  tags: icon.tags,
  aliases: icon.aliases,
}));

const generatedFileJson = JSON.stringify({
  mdi_version: getVersion(),
  meta: mappedIconMeta,
});
await writeFile(new URL("./meta.json", import.meta.url), generatedFileJson);
