import yaml
from flask import Flask

app = Flask(__name__)


def get_bookmarks_by_tag() -> dict:
    with open('/home/anthony/.config/bookmarks/bookmarks.yml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        output = {}
        for key in data:
            for tag in data[key]['tags']:
                if tag not in output.keys():
                    output[tag] = []

                output[tag].append({
                    'name': key,
                    'url': data[key]['url'],
                    'tags': data[key]['tags'],
                })
        return output


@app.route("/")
def hello_world():
    bookmarks_by_tag = get_bookmarks_by_tag()
    html = ''
    for tag in bookmarks_by_tag:
        html += f'<h1>{tag}</h1>'
        for bookmark in bookmarks_by_tag[tag]:
            html += '<div>'
            html += f'<a href={bookmark["url"]}>{bookmark["name"]}</a>'
            html += ' - tags: ['
            for bookmark_tag in bookmark['tags']:
                html += f'{bookmark_tag}, '
            html += ']</div>'
    return html
