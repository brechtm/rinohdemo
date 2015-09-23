.. This is a reStructuredText file describing the contents of an article
   to be typeset by RinohType.

=================
 About RinohType
=================

:author: Brecht Machiels
:organization: Opqode

:abstract:

    This article introduces RinohType and illustrates some of its features. The
    source for this document is a plain text file, marked up using the
    reStructuredText syntax which is briefly discussed in this article.


Introduction
============

RinohType is a batch document processor written in Python_. It can render
structured text documents to PDF based on a document template and a style sheet.
A structured text document is a document that describes the content of a
document without saying anything about how the resulting document should be
styled. For example, instead of marking some words to be rendered in an italic
font, they can be marked as being emphasized. Separating content and
presentation brings numerous advantages:

* it is easy to consistently change style aspects of a document without manual
  reworking of the document
* the document can be published from a single source to multiple formats: web,
  e-book, print, audio and braille for example
* the document can be automatically be reformatted to fit different page or
  screen sizes
* the document can be translated without the risk of breaking the styling
* the document is easier to index and search

.. source: https://en.wikipedia.org/wiki/Separation_of_presentation_and_content

The styling of the document is determined by the document template and style
sheet. These will be discussed in the next section.

.. _Python: http://www.python.org


Typesetting and Automation
==========================

Readability of text is improved by kerning glyphs and substituting ligatures.
Words can automatically be hyphenated, if the document's language is specified.
You can tag individual paragraphs or even words with a particular language so
that multi-language documents are properly hyphenated.

RinohType handles the automatic numbering of pages, sections and footnotes. The
numbering style (arabic or roman numerals, letters or symbols) is determined
by the style sheet used when rendering the document. Cross-references, normally
specified by means of IDs, can display the target's title or number, or the
number of the page the target is located on. Finally, RinohType automatically
generates the table of contents based on the sections present in the document.


Document Elements
=================

.. |inlineimg| image:: static/biohazard.png

RinohType supports all common document elements. Paragraphs may contain inline
markup such as *emphasis*, **strong emphasis** and ``inline literals``. You can
have :sub:`subscript`, :sup:`superscript` and even inline images (|inlineimg|).
Here's a hyperlink to the `Opqode website <http://www.opqode.com>`_. A
cross-reference to another section, such as `Document Templates`_ is also
represented as a hyperlink. This sentences includes a reference\ [1]_ for a
footnote at the bottom of this page.

.. [1] Footnotes are not limited to text. They can contain the same body
       elements that can also be used in the main text.

Paragraphs are one example of the many body elements supported by RinohType.
Other elements include nested lists, optionally enumerated.

- Bullet list item 1

  1. Nested enumerated list item 1
  2. Nested item 2

- Bullet list item 2

  Second paragraph of item 2


There are also other types of lists such as definition and field lists. Below
is an example of a definition list.

Term
    Definition
Term : classifier
    Definition paragraph 1.

    Definition paragraph 2.


Literal blocks are used for displaying source code snippets::

    class MumboJumbo(object):
        """A Python class"""

        def __init__(self, name):
            self.name = name


RinohType handles complex tables with cells spanning rows and/or columns. Table
columns can be sized automatically based on their contents.

.. table:: A table with caption

    +-------------+------------+------------+
    | Header 1    | Header 2   | Header 3   |
    +=============+============+============+
    | body row 1  | column 2   | column 3   |
    +-------------+------------+------------+
    | body row 2  | Cells may span columns  |
    +-------------+------------+------------+
    | body row 3  | Cells may  | * item     |
    +-------------+ span rows  | * item     |
    | body row 4  |            | * item     |
    +-------------+------------+------------+


RinohType natively supports PDF, PNG and JPEG images. Images in other formats
can be loaded if Pillow_ is available. Images with transparency are fully
supported. If present, embedded color profiles are preserved. Below, a bitmap
image is included.

.. image:: static/title.png

.. _Pillow: https://python-pillow.github.io

Images and tables can optionally be floated to the top or bottom of the page.
For images, this is done by wrapping the image in a figure along with a caption.
A vector image is included in a figure which floats to the top of this page.

.. figure:: static/python-powered-w.pdf
   :scale: 30%
   :alt: Python powered

   A figure is an image with a caption.

Selected paragraphs (or other body elements) can be made to stand out from the
rest of the document by placing it in a box. This is typically used to indicate
that the contents are important, or simply a way to visually differentiate
specific content, such as examples in textbooks.

.. WARNING:: Thou shalt not mix content and presentation!


If your document requires non-standard document elements, new *flowables* to
represent these can easily be built in Python using the building blocks included
with RinohType.


Style Sheets
============

RinohType makes use of style sheets to determine the presentation of a document.
Similar to the web's `Cascading Style Sheets`_ (CSS), RinohType's style sheets
set styling attributes for each of the elements in a document. However, whereas
in CSS the selection of these elements is also performed in the style sheet, in
RinohType the selection of elements is not part of the style sheet. A so-called
*matcher* maps element selectors to unique style names. The style sheet then
assigns style properties to these style names. This has the advantage that a
single matcher can be used by multiple style sheets. Another advantage is that
each style is assigned a descriptive style name, making altering existing style
sheets or creating new ones more accessible.

While RinohType's mechanism for selecting elements closely resembles CSS, the
inheritance model is fundamentally different. In CSS, a document element
inherits some style properties from its parent element. Only the style
properties for which this makes sense are inherited, such as font-related
properties. Still, this can cause some confusion. In RinohType, style
inheritance is more explicit. For each style defined in a style sheet, a base
style can be specified. If a particular style property is not defined in a style
definition, it will be retrieved from its base style (recursively). If the style
property is not defined anywhere in the style hierarchy, behavior differs
between inline and body elements. For body elements, the default for the style
property is returned. For inline elements (text elements that make up
paragraphs), the property value is retrieved from the parent element. This
applies to *all style properties* of text elements.

Finally, it is worth mentioning that RinohType style sheets have support for
variables, a feature sorely missing from CSS.

.. _Cascading Style Sheets: http://www.w3.org/Style/CSS/Overview.en.html


Document Templates
==================

Style sheets determine how individual elements are presented in the document.
Other aspects of the document's presentation are handled by the document
template. For example, the document template references one or page templates
that define areas where text and other document elements will appear. They
also define where headers, footers, footnotes and floats are placed.

The document template also describes the parts of which the document will
consist. Examples of document parts: title page, table of contents, preface,
chapters, appendices, index, bibliography. Each may use its own page template.

Document templates will typically be configurable. This allows tweaking certain
document presentation aspects such as the page size, page margings, the number
of columns and the header and footer text. RinohType currently comes with
basic configurable book and article templates. These will be enhanced as time
goes on.


Citations and Bibliography
==========================

For documents that reference other documents RinohType's sister-project
citeproc-py_ automates the formatting of citations and bibliographies. Simply
choose one of the 7500+ citations styles available from the CSL_ project,
reference other documents by ID, and citeproc will ensure that your citations
and bibliography are properly formatted.

.. _CSL: http://citationstyles.org
.. _citeproc-py: https://pypi.python.org/pypi/citeproc-py/


Frontends and Backends
======================

Thanks to its modular design, RinohType can be easily extended to support
other input and output formats.

.. TODO:: Sphinx

A frontend transforms the input document's native document tree to RinohType's
internal document tree. Already included with RinohType is a comprehensive
reStructuredText_ frontend. reStructuredText is a lightweight plain text markup
syntax that can be used to express a wide range of document types. It can be
unambiguously parsed by computer software, yet it still is comfortable to read
and write by humans, unlike XML. It relies on certain consistent patterns to
express many different types of document elements. The source of this article is
written in reStructuredText!

An important feature of reStructuredText is its extensibility. By defining new
roles* and *directives* custom elements can be added to the document. This
allows customizing your documents to your application domain. Defining
corresponding RinohType styles or even custom flowables determines how these new
document elements are represented in the final rendered document.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

Frontend for other formats will be added in the future. A DocBook_ frontend is
being developed. Other formats that are good candidates for a RinohType frontend
include DITA_ and HTMLBook_.

.. _DocBook: http://www.docbook.org/whatis
.. _DITA: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=dita
.. _HTMLBook: http://oreillymedia.github.io/HTMLBook/

Writing a frontend for a new document format is fairly straightforward, as it
merely needs to map each of the format's native doctree elements to the
corresponding RinohType's element. The reStructuredText frontend for example
takes up less than a 1000 lines of Python code.


Built on Python
===============

RinohType was initially developed as a modern replacement for LaTeX_. An
important goal in the design of RinohType is to improve upon LaTeX. More
specifically, RinohType should be much easier to customize. By today's
standards, the arcane TeX macro language upon which LaTeX is built makes
customization extremely difficult.

.. _LaTeX: https://www.latex-project.org

.. RinohType was initially developed as a modern replacement for LaTeX_. An
important goal in the design of RinohType is to improve upon LaTeX. More
specifically, RinohType should be much easier to use and customize. LaTeX is
notorious for its cryptic error messages, for example. And by today's standards,
the arcane TeX macro language upon which LaTeX is built makes customizing the
style of documents extremely difficult. Contrast this with RinohType's small,
modular Python code base, as discussed in the previous section,
`Built on Python`_. The use of `style sheets`_ and configurable
`document templates`_ allows for extensive customization even without the need
to write Python source code.

RinohType is written in Python_, an easy to learn, high-level programming
language. Python's elegance and RinohType's simple, modular design make it easy
to customize and extend for specific applications. Because RinohType is an open
source project (but not free for commercial use), all of its internals can be
inspected and modified, making it extremely customizable. Moreover, RinohType's
core source code consists of less than 4000 lines, making it very accessible to
interpretation and modification.

RinohType is a pure-Python application. This means that it does not rely on
any compiled extensions, making it very easy to deploy. Care is also taken to
minimize dependencies. For reStructuredText support, RinohType relies on
docutils_. For PNG support, PurePNG_ is needed. Both these are also pure-Python
packages.

.. _docutils: http://docutils.sourceforge.net
.. _PurePNG: http://purepng.readthedocs.org


Because RinohType does not rely on compiled extensions, it can be easily run on
alternative interpreters such as PyPy_, Jython_ and IronPython_. PyPy can run
Python applications at much higher speeds compared to the reference interpreter,
CPython. Jython and IronPython allow embedding Python software inside Java and
NET software. Unfortunately, both do not yet support version 3 of the Python
language which RinohType is written in. Depending on the interest in running
RinohType on these alternative Python implementations, RinohType might get
backported to Python 2.

.. _PyPy: http://pypy.org
.. _Jython: http://www.jython.org
.. _IronPython: http://ironpython.net


Applications
============

RinohType was originally designed for typesetting technical or scientific
documents. However, it is perfectly capable of publishing other types of
documents as well, as these are typically less complex in nature.

RinohType is especially suited for typesetting documents in a fully automated
way based on a document template and stylesheet. Examples include:

* (technical) books, manuals and articles
* marketing brochures
* product catalogues
* financial/test/QA reports
* data/fact sheets
* certificates

For books, manuals, articles and brochures, the document's content can be
described in XML or another structured text format in single-source publishing
workflow. This source document can optionally be automatically fetched from a
content management system. For other document such as catalogues or reports,
the content will typically originate from a database. As the database is updated
with new data, new documents can easily be generated without the need for manual
intervention. Some document types will require the combination of structured
text input and data fetched from a database.

RinohType can also be used where lower-level PDF libraries are typically used
for generating small PDF documents such as **invoices** and **tickets** on
websites. RinohType's advanced layout engine offers some advantages over PDF
libraries, while still being very lightweight.
