.. This is a reStructuredText file describing the contents of an
   article to be typeset by RinohType.

=================
 About RinohType
=================

:author: Brecht Machiels
:organization: Opqode

:abstract:

    This article introduces RinohType and illustrates some of
    its features. The source for this document is a plain text
    file, marked up using the reStructuredText syntax.


Introduction
============

RinohType is a batch document processor written in Python_. It
can render structured documents to PDF based on a document
template and a style sheet. A structured text document is a
document that describes the content of a document without saying
anything about how the resulting document should be styled. For
example, instead of marking some words to be rendered in an
italic font, they can be marked as being emphasized. Separating
content and presentation brings numerous advantages:

* it is easy to consistently change style aspects of a document
  without requiring manual reworking
* the document can be published from a single source to multiple
  formats: web, e-book, print, audio, braille, ...
* the document can be automatically reformatted to fit different
  page or screen sizes
* the document can be translated without the risk of breaking
  the styling
* the document is easier to index and search

The styling of the document is determined by the document
template and style sheet. These will be discussed in later
sections.

.. _Python: http://www.python.org


Typesetting and Automation
==========================

RinohType improves readability of text by *kerning* glyphs and
substituting *ligatures*. Words can automatically be
*hyphenated* if the document's language is specified. You can
tag individual paragraphs or even words with a particular
language so that multi-language documents are properly
hyphenated.

RinohType handles the *automatic numbering* of pages, sections
and footnotes. The numbering style (arabic or roman numerals,
letters or symbols) is determined by the style sheet.
Cross-references*, specified by means of IDs, can display the
target's title or number, or the number of the page the target
is located on. Finally, RinohType automatically generates the
*table of contents* based on the structure of the document.


Document Elements
=================

.. |inlineimg| image:: static/biohazard.png

RinohType supports all common document elements. Paragraphs may
contain inline markup such as *emphasis*, **strong emphasis**
and ``inline literals``. You can have :sub:`subscript`,
:sup:`superscript` and even inline images (|inlineimg|). Here's
a hyperlink to the `Opqode website <http://www.opqode.com>`_. A
cross-reference to another section, such as `Document
Templates`_ is also represented as a hyperlink. This sentence
includes a reference\ [1]_ to a footnote at the bottom of this
page.

.. [1] Footnotes are not limited to text. They can contain all
       elements that can also be used in the main text.

Paragraphs are one example of the many body elements supported
by RinohType. Other elements include nested lists which can
optionally be enumerated.

- Bullet list item 1

  1. Nested enumerated list item 1
  2. Nested item 2

- Bullet list item 2

  Second paragraph of item 2


There are also other types of lists such as definition and field
lists. Below is an example of a definition list.

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


RinohType can handle complex tables with cells spanning rows
and/or columns. Table columns can be sized automatically based
on their contents.

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


RinohType natively supports PDF, PNG and JPEG images. Images in
other formats can be loaded if Pillow_ is available. Images with
transparency are fully supported. Embedded color, if present,
profiles are preserved. Below, a bitmap image is included.

.. image:: static/title.png

.. _Pillow: https://python-pillow.github.io

Images and tables can optionally be floated to the top or bottom
of the page. For images, this is done by wrapping the image in a
figure along with a caption. A vector image is included in a
figure which floats to the top of this page.

.. figure:: static/python-powered-w.pdf
   :scale: 30%
   :alt: Python powered

   A figure is an image with a caption.

Selected paragraphs (or other body elements) can be made to
stand out from the rest of the document by placing it in a box.
This is typically used to indicate that the contents are
important, or simply to visually differentiate specific content,
such as examples in textbooks.

.. WARNING:: Thou shalt not mix content and presentation!


If your document requires non-standard elements, new so-called
*flowables* to represent these can easily be built in Python
using the building blocks included with RinohType.


Style Sheets
============

RinohType makes use of style sheets to determine the
presentation of the elements in a document. Similar to the web's
`Cascading Style Sheets`_ (CSS), these style sheets assign
styling properties to each of the elements in a document. In
RinohType the selection of elements is not part of the style
sheet as in CSS, however. A so-called *matcher* maps element
selectors to unique style names to which the style sheet then
assigns style properties. This has the advantage that a single
matcher can be used by multiple style sheets. Another advantage
is that each style is assigned a descriptive style name which
makes altering existing style sheets or creating new ones more
accessible.

While RinohType's mechanism for selecting elements closely
resembles CSS, the inheritance model is fundamentally different.
In CSS, a document element inherits some style properties from
its parent element. Only the style properties for which this
makes sense are inherited, such as font-related properties.
Still, this can cause some confusion. In RinohType, style
inheritance is more explicit. For each style defined in a style
sheet, a base style can be specified. If a particular style
property is not defined in a style definition, it will be
retrieved from its base style (recursively). If the style
property is not defined anywhere in the style hierarchy,
behavior differs between inline and body elements. For body
elements, the default value for the style property is returned.
For inline elements (text elements that make up paragraphs), the
property value is retrieved from the parent element. This
applies to *all style properties* of text elements.

Finally, it is worth mentioning that RinohType style sheets have
support for variables, a feature sorely missing from CSS.

.. _Cascading Style Sheets: http://www.w3.org/Style/CSS/Overview.en.html


Document Templates
==================

Style sheets determine how individual elements are presented in
the document. Other aspects of the document's presentation are
handled by the document template. For example, the document
template references one or more page templates that define areas
where text and other document elements will appear. They also
define where headers, footers, footnotes and floats are placed.

The document template also describes the parts of which the
document will consist. Examples of document parts: title pages,
table of contents, preface, chapters, appendices, index,
bibliography. Each may use its own page template.

Document templates can be configurable. This allows tweaking
certain document presentation aspects such as the page size,
page margings, the number of columns and the header and footer
text. RinohType currently comes with basic, but configurable
book and article templates which will be extended as time goes
on.


Citations and Bibliography
==========================

For documents that reference other documents RinohType's
sister-project citeproc-py_ automates the formatting of
citations and bibliographies. Simply choose one of the 7500+
citations styles available from the CSL_ project, reference
other documents by ID, and citeproc will ensure that your
citations and bibliography are properly ordered and formatted.

.. _CSL: http://citationstyles.org
.. _citeproc-py: https://pypi.python.org/pypi/citeproc-py/


Frontends and Backends
======================

Thanks to its modular design based on frontends and backends,
RinohType can be easily extended to support other input and
output formats. Currently, there is only a single backend, one
that produces PDF.

A frontend transforms the input document's native document tree
to RinohType's internal document tree. Included with RinohType
is a comprehensive reStructuredText_ frontend. reStructuredText
is a lightweight plain text markup syntax that can be used to
express a wide range of document types. It can be unambiguously
parsed by computer software, yet it still is comfortable to read
and write, in contrast to XML. It relies on certain consistent
patterns to express many different types of document elements.
The source of this very article is written in reStructuredText!

Building on reStructuredText, Sphinx_ is a tool that helps
organizing large documents by adding support for advanced
cross-references and index building, among others. It can output
documents in a multitude of formats including HTML. RinohType
can be used by Sphinx to output PDF.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Sphinx: http://sphinx-doc.org

Frontend for other formats will be added in the future. Work has
started on a DocBook_ frontend, for example. Other formats that
are good candidates for a RinohType frontend include DITA_ and
HTMLBook_.

.. _DocBook: http://www.docbook.org/whatis
.. _DITA: https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=dita
.. _HTMLBook: http://oreillymedia.github.io/HTMLBook/

Writing a frontend for a new document format is fairly
straightforward, as it merely needs to map each of the format's
native doctree elements to the corresponding RinohType
element. The reStructuredText frontend for example takes up less
than 1000 lines of Python code.


Built on Python
===============

RinohType was initially conveiced as a modern replacement for
LaTeX_. An important goal in the design of RinohType is to
improve upon LaTeX. More specifically, RinohType should be much
easier to customize. By today's standards, the arcane TeX macro
language upon which LaTeX is built makes customization extremely
difficult for one.

.. _LaTeX: https://www.latex-project.org

RinohType is written in Python_, an easy to learn, high-level
programming language. Python's elegance and RinohType's simple,
modular design make it easy to customize and extend for specific
applications. Because RinohType is an open source project (but
not free for commercial use), all of its internals can be
inspected and modified, making it extremely customizable.
Moreover, RinohType's core source code consists of less than
4000 lines, making it very accessible to interpretation and
modification.

RinohType is a pure-Python application. This means that it does
not rely on any compiled extensions and thus is very easy to
deploy. Care is also taken to minimize dependencies. For
reStructuredText support, RinohType relies on docutils_. For PNG
support, PurePNG_ is needed. Both these are also pure-Python
packages.

.. _docutils: http://docutils.sourceforge.net
.. _PurePNG: http://purepng.readthedocs.org

Because RinohType does not rely on compiled extensions, it can
be easily run on alternative interpreters such as PyPy_, Jython_
and IronPython_. PyPy can run Python applications at much higher
speeds compared to the reference interpreter, CPython. Jython
and IronPython allow embedding Python software inside Java and
.NET software. Unfortunately, both do not yet support version 3
of the Python language which RinohType is written in. Depending
on popular demand, RinohType might get backported to Python 2
however.

.. _PyPy: http://pypy.org
.. _Jython: http://www.jython.org
.. _IronPython: http://ironpython.net


Applications
============

RinohType was originally designed for typesetting technical or
scientific documents. However, it is perfectly capable of
publishing other types of documents as well, as these are
typically less complex in nature.

RinohType is especially suited for typesetting documents in a
fully automated way based on a document template and stylesheet.
Examples include:

* (technical) books, manuals and articles
* marketing brochures
* product catalogues
* financial/test/QA reports
* data/fact sheets
* certificates

For books, manuals, articles and brochures, the document's
content can be described using XML or another structured text
format. PDF can be just one of the output formats in a
single-source publishing workflow. The source document can
optionally be stored in a content management system.

For document such as catalogues or reports, the document content
will typically be fetched from a database. As the database is
updated with new data, new documents can easily be generated
without the need for manual intervention. Some document types
will require the combination of structured text input and data
fetched from a database.

RinohType can also be used where lower-level PDF libraries are
typically used for generating small PDF documents such as
*invoices* and *tickets* on websites. In this scenario
RinohType's advanced layout engine offers some advantages over
PDF libraries, while still being very lightweight.
