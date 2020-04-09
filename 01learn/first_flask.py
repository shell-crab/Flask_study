from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def test():
    return 'hello world'

@app.route('/book/<int:id>/')
def book(id):
    return f'book-{id}'

@app.route('/<any(bolg,guss):url_path>/<id>')
def item(url_path, id):
    if url_path == "blog":
        return f'blog-{id}'
    else:
        return f'guss-{id}'

@app.route('/article/')
def article():
    rev = request.args.get('id')
    return rev

@app.route('/user/')
def user():
    revp = request.form.get('username')
    return revp

if __name__ == "__main__":
    app.run(debug=True)