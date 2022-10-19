from urllib.request import urlopen
import json

config = {
    'icondialoglib_commit': "c561f68bf302a94626631d1930b88f4faf45528c",
    'mdi_commit': "e0f630048de499e2ed938b6374efffc7f752ce81"
}

def fetch_icon_dialog_id_mapping(commit):
    """
    Fetches a map of icon character codes to numeric IDs.
    The IDs are used by icondialoglib to identify icons.

    :param commit: Git commit hash of the maltaisn/icondialoglib repository to fetch.
    :return: A map of icon character codes to numeric IDs.
    """
    url = f"https://raw.githubusercontent.com/maltaisn/icondialoglib/{commit}/utils/mdi_id_map.json"
    data = json.loads(urlopen(url).read().decode("utf-8"))
    return {charcode.lower(): id for charcode, id in data.items()}

def fetch_mdi_meta(commit):
    """
    Fetches meta information from the Material Design Icons repository.

    :param commit: Git commit hash of the Templarian/MaterialDesign-SVG repository to fetch.
    :return: A list of meta information for each icon.
    """
    url = f"https://raw.githubusercontent.com/Templarian/MaterialDesign-SVG/{commit}/meta.json"
    return json.loads(urlopen(url).read().decode("utf-8"))


dialog_id_map = fetch_icon_dialog_id_mapping(config['icondialoglib_commit'])
icon_meta = fetch_mdi_meta(config['mdi_commit'])
compact_json_separators = (',', ':')

mapped_dialog_id_to_name = {
    icon['name']: dialog_id_map[icon['codepoint'].lower()]
    for icon in icon_meta if icon['codepoint'].lower() in dialog_id_map
}
with open("mdi_id_map.json", "w") as f:
    json.dump(mapped_dialog_id_to_name, f, separators=compact_json_separators)

mapped_icon_meta = [
    {
        'name': icon['name'],
        'codepoint': icon['codepoint'],
        'tags': icon['tags'],
        'aliases': icon['aliases'],
    } for icon in icon_meta
]
with open("icon_meta.json", "w") as f:
    json.dump(mapped_icon_meta, f, separators=compact_json_separators)
