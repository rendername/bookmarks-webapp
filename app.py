from flask import Flask

app = Flask(__name__)


def get_bookmarks_by_tag() -> dict:
    output = {}
    with open('/home/anthony/.config/bookmarks/bookmarks.txt', 'r') as f:
        for line in f.readlines():
            record = line.split(' ')
            tags = record[2].split(',')[0:-1]
            for tag in tags:
                if tag not in output.keys() and tag != '':
                    output[tag] = []

                output[tag].append({
                    'name': record[0],
                    'url': record[1],
                    'tags': tags,
                })
    return dict(sorted(output.items()))


@app.route("/")
def index():
    bookmarks_by_tag = get_bookmarks_by_tag()
    html = ''
    for tag in bookmarks_by_tag:
        html += f'<h1>{tag}</h1>'
        for bookmark in bookmarks_by_tag[tag]:
            html += '<div>'
            html += f'<a href=https://{bookmark["url"]} target="_blank">{bookmark["name"]}</a>'
            html += f' - tags: [{", ".join(bookmark["tags"])}]'
            html += '</div>'
    return html
