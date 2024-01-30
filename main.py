import yaml

def get_bookmarks_by_tag() -> dict:
    with open('/home/anthony/.config/bookmarks/bookmarks.yml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        output = {}
        for key in data:
            for tag in data[key]['tags']:
                if tag not in output.keys():
                    output[tag] = []

                output[tag].append(dict({
                    'name': key,
                }))
        return output

if __name__ == '__main__':
    print(get_bookmarks_by_tag())
