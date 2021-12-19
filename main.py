from flask import Flask, render_template, redirect, request, url_for
from data_parse.json_parser import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

info_parser = JsonParser('data\\feie.json')

 # href="/feie/{{item}}"
def main():
    app.run()


@app.route('/', methods=['GET'])
def index():
    return render_template("main_page.html", feie=info_parser.get_all())


@app.route('/feie/', methods=['GET'])
def feie():
    name = request.args.get('name')
    return render_template("feie.html", info=info_parser.get_feie(name))


@app.route('/about', methods=['GET'])
def about():
    return render_template("about.html")


@app.route('/links', methods=['GET'])
def links():
    return render_template("links.html")

if __name__ == '__main__':
    main()
