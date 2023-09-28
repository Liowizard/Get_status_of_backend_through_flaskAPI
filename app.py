from flask import Flask, render_template, Response
from flask_sse import sse

app = Flask(__name__)
app.register_blueprint(sse, url_prefix='/sse')

def generate_content():
    for i in range(1, 500000000000):
        if i % 5000000 == 0:
            yield f"data: {i}\n\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/content')
def content():
    return Response(generate_content(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
