import json
import requests
import os
import pkg_resources

def fetch_bst_files(json_path=None, save_dir='bst_styles'):
    if json_path is None:
        # Load from package resource
        json_path = pkg_resources.resource_filename('journal_abbrev', 'data/journals.json')

    with open(json_path, "r") as f:
        journal_data = json.load(f)

    os.makedirs(save_dir, exist_ok=True)
    for journal, info in journal_data.items():
        bst_url = info.get("bst_url")
        if bst_url:
            try:
                response = requests.get(bst_url, timeout=10)
                if response.status_code == 200:
                    filename = os.path.join(save_dir, f"{journal.replace(' ', '_')}.bst")
                    with open(filename, "wb") as f_out:
                        f_out.write(response.content)
                    print(f"Downloaded: {journal}")
                else:
                    print(f"Failed to download {journal}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error downloading {journal}: {e}")


