
from os import path

from rinoh.color import HexColor, BLACK
from rinoh.dimension import PERCENT, PT, CM
from rinoh.float import InlineImage
from rinoh.font import TypeFace, TypeFamily
from rinoh.font.style import REGULAR, ITALIC, LIGHT, BOLD
from rinoh.font.opentype import OpenTypeFont
from rinoh.paper import A4
from rinoh.paragraph import LEFT, TabStop, RIGHT, ProportionalSpacing
from rinoh.reference import Variable, PAGE_NUMBER, SECTION_TITLE
from rinoh.style import StyleSheet, Var
from rinoh.table import MIDDLE
from rinoh.text import Tab

from rinohlib.stylesheets.sphinx import stylesheet as SPHINX
from rinohlib.templates.article import ArticleOptions, TITLE


stylesheet = StyleSheet('RinohDemo', base=SPHINX)

# def os_filename(variant):
#     return path.join(path.dirname(__file__),
#                      path.pardir, path.pardir, path.pardir, 'rinohdemo',
#                      'fonts', 'OpenSans-{}.ttf'.format(variant))
#
# os_regular = OpenTypeFont(os_filename('Regular'), weight=REGULAR)
# os_italic = OpenTypeFont(os_filename('Italic'), weight=REGULAR, slant=ITALIC)
# os_light = OpenTypeFont(os_filename('Light'), weight=LIGHT)
# os_bold = OpenTypeFont(os_filename('Bold'), weight=BOLD)
#
# open_sans = TypeFace('TeXGyrePagella', os_regular, os_italic, os_light, os_bold)
#
# stylesheet.variables['fonts'] = TypeFamily(serif=open_sans,
#                                            sans=SPHINX.variables['fonts'].sans,
#                                            mono=SPHINX.variables['fonts'].mono)

stylesheet.variables['title_color'] = HexColor('#4466FF')
# stylesheet.variables['title_color'] = HexColor('#2F455A')
# stylesheet.variables['title_color'] = HexColor('#42617e')
# stylesheet.variables['title_color'] = HexColor('#537a9f')


stylesheet('chapter', base=SPHINX['chapter'],
           page_break=None)

stylesheet('heading level 1', base=SPHINX['heading level 1'],
           font_size=14*PT,
           font_color=Var('title_color'),
           number_format=None)

stylesheet('table of contents title', base='heading level 1',
           space_above=0)

stylesheet('header', base=SPHINX['header'],
           font_weight=REGULAR)
stylesheet('footer', base='header')

stylesheet('title',
           space_above=3*CM,
           space_below=0.8*CM,
           typeface=Var('fonts').serif,
           font_size=32*PT,
           font_weight=BOLD,
           font_color=Var('title_color'),
           justify=LEFT)

stylesheet('topic',
           margin_left=0)

stylesheet('abstract paragraph',
           base='default',
           justify=LEFT,
           font_size=12*PT,
           font_color=Var('title_color'),
           line_spacing=ProportionalSpacing(1.2))

stylesheet('table of contents',
           base='default',
           indent_first=0,
           depth=1)

stylesheet('toc level 1',
           base='table of contents',
           font_weight=BOLD,
           space_above=0*PT,
           show_number=False,
           tab_stops=[TabStop(1.0, RIGHT, fill='.  ')])

stylesheet('enumerated list', base=SPHINX['enumerated list'],
           margin_left=0,
           flowable_spacing=3*PT)

stylesheet('figure', base=SPHINX['figure'],
           space_below=20*PT)

stylesheet('table with caption',
           space_above=12*PT,
           space_below=8*PT)

stylesheet('table cell',
           space_above=2*PT,
           space_below=2*PT,
           margin_left=4*PT,
           margin_right=4*PT,
           vertical_align=MIDDLE)

stylesheet('table cell left border',
           stroke_width=0.5*PT,
           stroke_color=BLACK)

stylesheet('table cell top border',
           base='table cell left border')

stylesheet('table cell right border',
           base='table cell left border')

stylesheet('table cell bottom border',
           base='table cell left border')

stylesheet('table body cell background on even row',
           fill_color=None)

stylesheet('table head cell left border',
           stroke_color=None)

stylesheet('table head cell right border',
           base='table head cell left border')

stylesheet('table head bottom border',
           stroke_width=1*PT,
           stroke_color=BLACK)

stylesheet('table head left border',
           stroke_color=None)

stylesheet('table head right border',
           base='table head left border')

stylesheet('table top border',
           stroke_color=None)

stylesheet('table bottom border',
           stroke_width=1*PT,
           stroke_color=BLACK)

stylesheet('table left border',
           base='table bottom border')

stylesheet('table right border',
           base='table bottom border')

stylesheet('admonition', base=SPHINX['admonition'],
           stroke_width=None)


HEADER_TEXT = 'About RinohType' + Tab() + Tab() + Variable(SECTION_TITLE(1))
FOOTER_TEXT = (InlineImage('static/opqode_logo.pdf', scale=0.7,
                           baseline=31.5*PERCENT)
               + Tab() + Tab() + 'page ' + Variable(PAGE_NUMBER))


OPTIONS = ArticleOptions(page_size=A4, columns=2, table_of_contents=True,
                         header_text=HEADER_TEXT, footer_text=FOOTER_TEXT,
                         stylesheet=stylesheet, abstract_location=TITLE,
                         show_date=False, show_author=False)
