import os

from io import BytesIO, StringIO

from flask import Flask, request, send_file

from rinoh.backend import pdf
from rinoh.frontend.rst import ReStructuredTextParser

from rinohlib.templates.article import Article

from template import OPTIONS


os.chdir(os.path.dirname(__file__))


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


DEV_MODE = app.config['HOST_NAME'] == 'localhost'


@app.route('/', methods=['POST'])
def index():
    return render_and_send(request.form, as_attachment=True)


@app.route('/', methods=['GET'])
def test_index():
    data = {'filename': 'article'}
    with open('static/article.rst') as article:
        data['content'] = article.read()
    return render_and_send(data, as_attachment=False)


def render_and_send(form_data, as_attachment=True):
    pdf_output = render_rst(form_data['content'])
    response = send_file(pdf_output, as_attachment=as_attachment,
                         attachment_filename=form_data['filename'] + '.pdf',
                         mimetype='application/pdf')
    response.headers.add('content-length', str(pdf_output.getbuffer().nbytes))
    return response


def render_rst(content):
    input_file = StringIO(content)
    parser = ReStructuredTextParser()
    document_tree = parser.parse(input_file)
    document = Article(document_tree, OPTIONS, backend=pdf)
    pdf_output = BytesIO()
    document.render(file=pdf_output)
    pdf_output.seek(0)
    return pdf_output


ALLOW_ORIGIN = '*' if DEV_MODE else 'http://www.opqode.com'


def article_allow_origin(response):
    """Allow article.rst to be fetched by the opqode website"""
    if request.path == '/static/article.rst':
        response.headers.add('Access-Control-Allow-Origin', ALLOW_ORIGIN)
    return response


app.after_request(article_allow_origin)


if __name__ == '__main__':
    app.run(debug=True)
