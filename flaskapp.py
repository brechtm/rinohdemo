import json

from io import BytesIO, StringIO

from flask import Flask, request, send_file

from rinoh.backend import pdf
from rinoh.frontend.rst import ReStructuredTextParser

from rinohlib.templates.article import Article

from template import OPTIONS


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/', methods=['POST'])
def index():
    return render_and_send(request.form, as_attachment=True)


@app.route('/', methods=['GET'])
def test_index():
    data = {}
    with open('../opqode.com/article.rst') as article:
        data['content'] = article.read()
    return render_and_send(data, as_attachment=False)


TEST_DATA = dict(content="""
Title
=====

First Section
-------------

Hello *world*.

Second Section
--------------

Goodbye world.

""")


def render_and_send(form_data, as_attachment=True):
    pdf_output = render_rst(form_data)
    response = send_file(pdf_output, as_attachment=as_attachment,
                         attachment_filename='output.pdf',
                         mimetype='application/pdf')
    response.headers.add('content-length', str(pdf_output.getbuffer().nbytes))
    print(response.headers)
    return response


def render_rst(data):
    input_file = StringIO(data['content'])
    parser = ReStructuredTextParser()
    document_tree = parser.parse(input_file)
    document = Article(document_tree, OPTIONS, backend=pdf)
    pdf_output = BytesIO()
    document.render(file=pdf_output)
    pdf_output.seek(0)
    return pdf_output


if __name__ == '__main__':
    app.run()
