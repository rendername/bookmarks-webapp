import json
import yaml

def load_file():
    with open("/home/anthony/.config/bookmarks/Bookmarks", "r") as f:
        return json.load(f)['roots']['bookmark_bar']['children']

if __name__ == '__main__':
    # yaml style
    # name:
    #   url: url_value
    #   tags: [tag_values]
    output = {}
    for folder in load_file():
        for bookmark in folder['children']:
            output[bookmark['name']] = {
                'url': bookmark['url'],
                'tags': [folder['name']],
            }
    print(yaml.dump(output))
