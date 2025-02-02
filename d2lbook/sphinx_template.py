
sphinx_conf = r"""
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '.')

project = "TITLE"
copyright = "COPYRIGHT"
author = "AUTHOR"
release = "RELEASE"

extensions = [EXTENSIONS]

# Customize bibtext_reference_style: https://github.com/mcmtroffaes/sphinxcontrib-bibtex/blob/develop/doc/usage.rst
from dataclasses import dataclass, field
import sphinxcontrib.bibtex.plugin

from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year \
    import AuthorYearReferenceStyle
def bracket_style() -> BracketStyle:
    return BracketStyle(
        left='(',
        right=')',
    )
@dataclass
class MyReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)
sphinxcontrib.bibtex.plugin.register_plugin(
    'sphinxcontrib.bibtex.style.referencing',
    'author_year_round', MyReferenceStyle)

# For original square brackets, just set bibtex_reference_style = 'author_year'
# If unspecified, citet output will be "Zhang et al. [Zhang et al. 2022]" instead of "Zhang et al. (2022)"
bibtex_reference_style = 'author_year_round'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'INDEX'
numfig = True
numfig_secnum_depth = 2
math_numfig = True
math_number_all = True

suppress_warnings = ['misc.highlighting_failure']
linkcheck_ignore = [r'.*localhost.*']
linkcheck_timeout = 5
linkcheck_workers = 20

autodoc_default_options = {
    'undoc-members': True,
    'show-inheritance': True,
}


html_theme = 'mxtheme'
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'header_links': [
        HEADER_LINKS
    ],
    'show_footer': False
}
html_static_path = ['_static']

html_favicon = 'FAVICON'

html_logo = 'HTML_LOGO'

latex_documents = [
    (master_doc, "NAME.tex", "TITLE",
     author, 'manual'),
]

rsvg_converter_args = ['-z', '0.8']
bibtex_bibfiles = ["BIBFILE"]
latex_engine = 'xelatex' # for utf-8 supports
latex_show_pagerefs = True
latex_show_urls = 'footnote'

latex_logo = 'LATEX_LOGO'

latex_elements = {

'figure_align': 'H',

'pointsize': '11pt',
'preamble': r'''

% Page size
\setlength{\voffset}{-14mm}
\addtolength{\textheight}{16mm}

% Chapter title style
\usepackage{titlesec, blindtext, color}
\definecolor{gray75}{gray}{0.75}
\newcommand{\hsp}{\hspace{20pt}}
\titleformat{\chapter}[hang]{\Huge\bfseries}{\thechapter\hsp\textcolor{gray75}{|}\hsp}{0pt}{\Huge\bfseries}

% So some large pictures won't get the full page
\renewcommand{\floatpagefraction}{.8}

\setcounter{tocdepth}{1}
% Use natbib's citation style, e.g. (Li and Smola, 16)
\usepackage{natbib}
\protected\def\sphinxcite{\citep}

MAIN_FONT
SANS_FONT
MONO_FONT

% Remove top header
\setlength{\headheight}{13.6pt}
\makeatletter
    \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
        \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
        \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
        \fancyhead[LE,RO]{{\py@HeaderFamily }}
     }
\makeatother
% Defines macros for code-blocks styling
\definecolor{d2lbookOutputCellBackgroundColor}{RGB}{255,255,255}
\definecolor{d2lbookOutputCellBorderColor}{rgb}{.85,.85,.85}
\def\diilbookstyleoutputcell
   {\sphinxcolorlet{VerbatimColor}{d2lbookOutputCellBackgroundColor}%
    \sphinxcolorlet{VerbatimBorderColor}{d2lbookOutputCellBorderColor}%
    \sphinxsetup{verbatimwithframe,verbatimborder=0.5pt}%
   }%
%
\definecolor{d2lbookInputCellBackgroundColor}{rgb}{.95,.95,.95}
\def\diilbookstyleinputcell
   {\sphinxcolorlet{VerbatimColor}{d2lbookInputCellBackgroundColor}%
    \sphinxsetup{verbatimwithframe=false,verbatimborder=0pt}%
   }%
% memo: as this mark-up uses macros not environments we have to reset all changed
%       settings at each input cell to not inherit those or previous output cell
% memo: Sphinx 5.1.0, 5.1.1 ignore verbatimwithframe Boolean, so for this
%       reason we added an extra verbatimborder=0pt above.

''',

'sphinxsetup': '''verbatimsep=2mm,
                  VerbatimColor={rgb}{.95,.95,.95},
                  VerbatimBorderColor={rgb}{.95,.95,.95},
                  pre_border-radius=3pt,
               ''',
}
# memo: Sphinx 5.1.0+ has a "feature" that if we don't set VerbatimColor to
# some value via the sphinxsetup key or via \sphinxsetup raw macro, it
# considers no colouring of background is required.  Above we by-passed usage
# of \sphinxsetup, because \sphinxcolorlet was more convenient.  So we set
# VerbatimColor in 'sphinxsetup' global key to work around that "feature".
# The exact same applies with VerbatimBorderColor: it has to be set at least
# once via 'sphinxsetup' or via \sphinxsetup raw macro else frame is black.
#
# memo: the Sphinx 5.1.0+ added pre_border-radius must be used in 'sphinxsetup'
# (it can be modified later via extra  raw \sphinxsetup)
# because at end of preamble Sphinx decides whether or not to load extra package
# for rendering boxes with rounded corners.  N.B.: pre_border-radius is
# unknown in Sphinx < 5.1.0 and will cause breakage.

SPHINX_CONFIGS

def setup(app):
    # app.add_js_file('https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js')
    app.add_js_file('d2l.js')
    app.add_css_file('d2l.css')
    import mxtheme
    app.add_directive('card', mxtheme.CardDirective)
"""

sphinx_conf_cambridge = r"""
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '.')

project = "TITLE"
copyright = "COPYRIGHT"
author = "AUTHOR"
release = "RELEASE"

extensions = [EXTENSIONS]

# Customize bibtext_reference_style: https://github.com/mcmtroffaes/sphinxcontrib-bibtex/blob/develop/doc/usage.rst
from dataclasses import dataclass, field
import sphinxcontrib.bibtex.plugin

from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year \
    import AuthorYearReferenceStyle
def bracket_style() -> BracketStyle:
    return BracketStyle(
        left='(',
        right=')',
    )
@dataclass
class MyReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)
sphinxcontrib.bibtex.plugin.register_plugin(
    'sphinxcontrib.bibtex.style.referencing',
    'author_year_round', MyReferenceStyle)

# For original square brackets, just set bibtex_reference_style = 'author_year'
# If unspecified, citet output will be "Zhang et al. [Zhang et al. 2022]" instead of "Zhang et al. (2022)"
bibtex_reference_style = 'author_year_round'





templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'INDEX'
numfig = True
numfig_secnum_depth = 2
math_numfig = True
math_number_all = True

suppress_warnings = ['misc.highlighting_failure']
linkcheck_ignore = [r'.*localhost.*']
linkcheck_timeout = 5
linkcheck_workers = 20

autodoc_default_options = {
    'undoc-members': True,
    'show-inheritance': True,
}


html_theme = 'mxtheme'
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'header_links': [
        HEADER_LINKS
    ],
    'show_footer': False
}
html_static_path = ['_static']

html_favicon = 'FAVICON'

html_logo = 'HTML_LOGO'

latex_documents = [
    (master_doc, "NAME.tex", "TITLE",
     author, 'PT1'),
]



rsvg_converter_args = ['-z', '0.8']

bibtex_bibfiles = ["BIBFILE"]

latex_engine = 'xelatex' # for utf-8 supports
latex_show_pagerefs = True
latex_show_urls = 'footnote'

latex_logo = 'LATEX_LOGO'

latex_elements = {
'papersize':'a4paper,prodtf,twoside',
'figure_align': 'htbp',
'pointsize': '11pt',
'fvset':r'''\fvset{fontsize=\small}''',
'preamble': r'''
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsthm}
\usepackage{color}
\usepackage[figuresright]{rotating}
\usepackage{floatpag}
\rotfloatpagestyle{empty}
\usepackage{makeidx}
\usepackage{natbib}
\usepackage[parfill]{parskip}
\usepackage{titlesec}
\usepackage{multicol}
\usepackage{fixmath}
\protected\def\sphinxcite{\citep}

% Add bib to TOC
\usepackage[nottoc,numbib]{tocbibind}

% QR code sidenotes for all footnotes
% Make sure to replace special charactors URL Encoding: https://www.urlencoder.io/learn/
\usepackage{sidenotes}
\usepackage{marginfix}
\setlength\marginparpush{20pt}
\usepackage{qrcode}
\newcommand{\qrsidenote}[1]{
\sidenote{
\qrcode[height=8mm]{#1}}
}
\newcommand{\relaxfootnote}[1][]{}

\makeatletter
\let\ps@normal\ps@headings
\let\sphinxthebibliography\thebibliography
\let\sphinxtheindex\theindex
\let\sphinxAtStartFootnote\!
\let\footnote\relaxfootnote
\let\sphinxnolinkurl\qrsidenote

\sphinxDeclareColorOption{TitleColor}{{rgb}{0,0,0}}
\sphinxDeclareColorOption{InnerLinkColor}{{rgb}{0,0,0}}
\sphinxDeclareColorOption{OuterLinkColor}{{rgb}{0,0,0}}

% So some large pictures won't get the full page
\renewcommand{\floatpagefraction}{.8}

% Set the page margin size
\geometry{left=1.9in, right=1.4in, includefoot, bottom=0.5in}

% Section and subsection style
\titleformat{\section}{\LARGE\centering\bfseries}{\thesection}%
            {0.5em}{}[{\hspace{-1.65in}\raggedleft\includegraphics[width=35pc]{PT1secrule.pdf}}]
\titleformat{\subsection}{\Large\centering\bfseries}%
            {\thesubsection}{0.5em}{}[{\color{gray}\titlerule[0.8pt]}]
\titleformat{\subsubsection}{\large\centering\bfseries}%
            {\thesubsubsection}{0.5em}{}[{\color{gray}}]

% Code font style, for more font style, visit: https://tug.org/FontCatalogue/
\setmonofont{Inconsolata}
%\renewcommand\ttfamily{\sffamily}

% Replace mathbf with mathbold
\renewcommand{\mathbf}[1]{\mathbold{#1}}

% Resize all figures
\let\ORIincludegraphics\includegraphics
\renewcommand{\includegraphics}[2][]{\ORIincludegraphics[scale=0.75,#1]{#2}}
% main text font style
\usepackage{times}

% Rewrite table of contents
\renewcommand\tableofcontents{\@restonecolfalse
 \if@twocolumn\@restonecoltrue\onecolumn\fi
 %\AJW@addtocfalse
 \chapter*{\contentsname}
 %\@starttoc{toc}
 %\AJW@addtoctrue
 \if@restonecol\twocolumn\fi
  \@starttoc{toc}
}

\newcommand\cambridge{PT1}
\theoremstyle{plain}% default
\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem*{corollary}{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{condition}[theorem]{Condition}
\newtheorem{example-norules}[theorem]{Example}
\theoremstyle{remark}
\newtheorem*{remark}{Remark}
\newtheorem*{case}{Case}


\hyphenation{line-break line-breaks docu-ment triangle cambridge
    amsthdoc cambridgemods baseline-skip author authors
    cambridgestyle en-vir-on-ment polar astron-omers solu-tion}

\setcounter{tocdepth}{1}

\hbadness=99999  % or any number >=10000
\vfuzz=30pt
\hfuzz=30pt

% Defines macros for code-blocks styling
\definecolor{d2lbookOutputCellBackgroundColor}{RGB}{255,255,255}
\definecolor{d2lbookOutputCellBorderColor}{rgb}{.85,.85,.85}
\def\diilbookstyleoutputcell
   {\sphinxcolorlet{VerbatimColor}{d2lbookOutputCellBackgroundColor}%
    \sphinxcolorlet{VerbatimBorderColor}{d2lbookOutputCellBorderColor}%
    \sphinxsetup{verbatimwithframe,verbatimborder=0.5pt}%
   }%
%
\definecolor{d2lbookInputCellBackgroundColor}{rgb}{.95,.95,.95}
\def\diilbookstyleinputcell
   {\sphinxcolorlet{VerbatimColor}{d2lbookInputCellBackgroundColor}%
    \sphinxsetup{verbatimwithframe=false,verbatimborder=0pt}%
   }%

''',
'sphinxsetup': '''verbatimsep=2mm,
                  VerbatimColor={rgb}{.95,.95,.95},
                  VerbatimBorderColor={rgb}{.95,.95,.95},
                  pre_border-radius=3pt,
               ''',
'maketitle':'\\maketitle',
'tableofcontents': '\\tableofcontents',
'fncychap':'',
'makeindex':'\\makeindex'
}


latex_style_loc = "static/latex_style/"
latex_fnames = ["PT1/PT1.cls", "PT1header.eps", "PT1secrule.pdf", "PT1/PT1box.eps", "PT1/PT1chrule.eps", "PT1/multind.sty",  "PT1/amsthm.sty", "PT1/floatpag.sty", "PT1/rotating.sty", "PT1/myriad-pt1.sty", "PT1/natbib.sty",  "sphinxlatexstyleheadings.sty", "sphinxlatexstylepage.sty", "sphinxlatexindbibtoc.sty", "sphinxmessages.sty", "sphinxlatexobjects.sty", "PT1/natbib.dtx", "sphinxpackagefootnote.sty", "sphinxlatexlists.sty"]
latex_additional_files = [latex_style_loc + fname for fname in latex_fnames]

SPHINX_CONFIGS

def setup(app):
    # app.add_js_file('https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js')
    app.add_js_file('d2l.js')
    app.add_css_file('d2l.css')
    import mxtheme
    app.add_directive('card', mxtheme.CardDirective)
"""


google_tracker = """
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

ga('create', 'GOOGLE_ANALYTICS_TRACKING_ID', 'auto');
ga('send', 'pageview');
var captureOutboundLink = function(url) {
   ga('send', 'event', 'outbound', 'click', url, {
     'transport': 'beacon',
     'hitCallback': function(){document.location = url;}
   });
}

var tagClick = function(tab) {
    ga('send', 'event', 'tab', 'click', tab, {
        'transport': 'beacon'
    });
}
"""

shorten_sec_num = """
$(document).ready(function () {
    $('.localtoc').each(function(){
        $(this).find('a').each(function(){
            $(this).html($(this).html().replace(/^\d+\.\d+\./, ''))
        });
    });
});
"""

# Replace the QR code with an embeded discussion thread.
replace_qr = """
$(document).ready(function () {
    $('h2').each(function(){
        if ($(this).text().indexOf("Discuss") != -1) {
            var url = $(this).find('a').attr('href');
            var tokens = url.split('/');
            var topic_id = tokens[tokens.length-1];
            var domain = tokens[0]+'//'+tokens[2]+'/';
            $(this).parent().append('<div id="discourse-comments"></div>');

            $('img').each(function(){
                if ($(this).attr('src').indexOf("qr_") != -1) {
                    $(this).hide();
                }
            });

            DiscourseEmbed = { discourseUrl: domain, topicId: topic_id };
            (function() {
                var d = document.createElement('script'); d.type = 'text/javascript';
                d.async = true;
                d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js';
                (document.getElementsByTagName('head')[0] ||
                 document.getElementsByTagName('body')[0]).appendChild(d);
            })();
        }
    });
});
"""

# CSS style to hide the bibkey but allow highlight
hide_bibkey_css = r"""
dl.citation > dt.label {
    width: 100%;
}

dl.citation span.brackets {
    padding-right: .8em;
}
"""

discourse_js = r"""
function discourse_embed() {
    $('a').each(function(){
        if ($(this).text().indexOf("Discussions") != -1) {
            var pp = $(this).parent();
            if (pp.is('h2')  || pp.is('li')) {
                return;
            }
            var pp = $(this).parent().parent();
            if (pp.hasClass('mdl-tabs__panel') && !pp.hasClass('is-active')) {
                return;
            }
            var url = $(this).attr('href');
            var tokens = url.split('/');
            var topic_id = tokens[tokens.length-1];
            var domain = tokens[0]+'//'+tokens[2]+'/';
            $("#discourse-comments").remove();
            $(this).parent().append('<div id="discourse-comments"></div>');


            DiscourseEmbed = { discourseUrl: domain, topicId: topic_id };
            (function() {
                var d = document.createElement('script'); d.type = 'text/javascript';
                d.async = true;
                d.src = DiscourseEmbed.discourseUrl + 'javascripts/embed.js';
                (document.getElementsByTagName('head')[0] ||
                 document.getElementsByTagName('body')[0]).appendChild(d);
            })();
            $(this).hide()
        }
    });
}
"""

tabbar_js = r"""
function select_tab(i) {
    var n = 4;
    $(".mdl-tabs").each(function(index){
        var j;
        for (j = 0; j < n; j++) {
            if (j != i) {
                $(this).find(".mdl-tabs__panel:eq("+j.toString()+")").removeClass('is-active');
            }
        }
        $(this).find(".mdl-tabs__panel:eq("+i.toString()+")").addClass('is-active');
    });
    $(".d2l-tabs").each(function(index){
        var j;
        for (j = 0; j < n; j++) {
            if (j != i) {
                $(this).find(".d2l-tabs__tab:eq("+j.toString()+")").hide();
            }
        }
        $(this).find(".d2l-tabs__tab:eq("+i.toString()+")").show();
    });
    $(".mdl-tabs__tab-bar").each(function(index){
        var j;
        for (j = 0; j < n; j++) {
            if (j != i) {
                $(this).find(".mdl-tabs__tab:eq("+j.toString()+")").removeClass('is-active');
            }
        }
        $(this).find(".mdl-tabs__tab:eq("+i.toString()+")").addClass('is-active');
    });
    discourse_embed();
}

$(document).ready(function () {
  select_tab(0);
  $(".mdl-tabs__tab-bar").each(function(index){
    $(this).find(".mdl-tabs__tab:eq(0)").click(function() {
        select_tab(0);
    });
    $(this).find(".mdl-tabs__tab:eq(1)").click(function() {
        select_tab(1);
    });
    $(this).find(".mdl-tabs__tab:eq(2)").click(function() {
        select_tab(2);
    });
    $(this).find(".mdl-tabs__tab:eq(3)").click(function() {
        select_tab(3);
    });
  });
});
"""
copybutton_js = r"""

!function(t,e){"object"==typeof exports&&"object"==typeof module?module.exports=e():"function"==typeof define&&define.amd?define([],e):"object"==typeof exports?exports.ClipboardJS=e():t.ClipboardJS=e()}(this,function(){return function(t){function e(o){if(n[o])return n[o].exports;var r=n[o]={i:o,l:!1,exports:{}};return t[o].call(r.exports,r,r.exports,e),r.l=!0,r.exports}var n={};return e.m=t,e.c=n,e.i=function(t){return t},e.d=function(t,n,o){e.o(t,n)||Object.defineProperty(t,n,{configurable:!1,enumerable:!0,get:o})},e.n=function(t){var n=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(n,"a",n),n},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="",e(e.s=3)}([function(t,e,n){var o,r,i;!function(a,c){r=[t,n(7)],o=c,void 0!==(i="function"==typeof o?o.apply(e,r):o)&&(t.exports=i)}(0,function(t,e){"use strict";function n(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}var o=function(t){return t&&t.__esModule?t:{default:t}}(e),r="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},i=function(){function t(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}return function(e,n,o){return n&&t(e.prototype,n),o&&t(e,o),e}}(),a=function(){function t(e){n(this,t),this.resolveOptions(e),this.initSelection()}return i(t,[{key:"resolveOptions",value:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};this.action=t.action,this.container=t.container,this.emitter=t.emitter,this.target=t.target,this.text=t.text,this.trigger=t.trigger,this.selectedText=""}},{key:"initSelection",value:function(){this.text?this.selectFake():this.target&&this.selectTarget()}},{key:"selectFake",value:function(){var t=this,e="rtl"==document.documentElement.getAttribute("dir");this.removeFake(),this.fakeHandlerCallback=function(){return t.removeFake()},this.fakeHandler=this.container.addEventListener("click",this.fakeHandlerCallback)||!0,this.fakeElem=document.createElement("textarea"),this.fakeElem.style.fontSize="12pt",this.fakeElem.style.border="0",this.fakeElem.style.padding="0",this.fakeElem.style.margin="0",this.fakeElem.style.position="absolute",this.fakeElem.style[e?"right":"left"]="-9999px";var n=window.pageYOffset||document.documentElement.scrollTop;this.fakeElem.style.top=n+"px",this.fakeElem.setAttribute("readonly",""),this.fakeElem.value=this.text,this.container.appendChild(this.fakeElem),this.selectedText=(0,o.default)(this.fakeElem),this.copyText()}},{key:"removeFake",value:function(){this.fakeHandler&&(this.container.removeEventListener("click",this.fakeHandlerCallback),this.fakeHandler=null,this.fakeHandlerCallback=null),this.fakeElem&&(this.container.removeChild(this.fakeElem),this.fakeElem=null)}},{key:"selectTarget",value:function(){this.selectedText=(0,o.default)(this.target),this.copyText()}},{key:"copyText",value:function(){var t=void 0;try{t=document.execCommand(this.action)}catch(e){t=!1}this.handleResult(t)}},{key:"handleResult",value:function(t){this.emitter.emit(t?"success":"error",{action:this.action,text:this.selectedText,trigger:this.trigger,clearSelection:this.clearSelection.bind(this)})}},{key:"clearSelection",value:function(){this.trigger&&this.trigger.focus(),window.getSelection().removeAllRanges()}},{key:"destroy",value:function(){this.removeFake()}},{key:"action",set:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"copy";if(this._action=t,"copy"!==this._action&&"cut"!==this._action)throw new Error('Invalid "action" value, use either "copy" or "cut"')},get:function(){return this._action}},{key:"target",set:function(t){if(void 0!==t){if(!t||"object"!==(void 0===t?"undefined":r(t))||1!==t.nodeType)throw new Error('Invalid "target" value, use a valid Element');if("copy"===this.action&&t.hasAttribute("disabled"))throw new Error('Invalid "target" attribute. Please use "readonly" instead of "disabled" attribute');if("cut"===this.action&&(t.hasAttribute("readonly")||t.hasAttribute("disabled")))throw new Error('Invalid "target" attribute. You can\'t cut text from elements with "readonly" or "disabled" attributes');this._target=t}},get:function(){return this._target}}]),t}();t.exports=a})},function(t,e,n){function o(t,e,n){if(!t&&!e&&!n)throw new Error("Missing required arguments");if(!c.string(e))throw new TypeError("Second argument must be a String");if(!c.fn(n))throw new TypeError("Third argument must be a Function");if(c.node(t))return r(t,e,n);if(c.nodeList(t))return i(t,e,n);if(c.string(t))return a(t,e,n);throw new TypeError("First argument must be a String, HTMLElement, HTMLCollection, or NodeList")}function r(t,e,n){return t.addEventListener(e,n),{destroy:function(){t.removeEventListener(e,n)}}}function i(t,e,n){return Array.prototype.forEach.call(t,function(t){t.addEventListener(e,n)}),{destroy:function(){Array.prototype.forEach.call(t,function(t){t.removeEventListener(e,n)})}}}function a(t,e,n){return u(document.body,t,e,n)}var c=n(6),u=n(5);t.exports=o},function(t,e){function n(){}n.prototype={on:function(t,e,n){var o=this.e||(this.e={});return(o[t]||(o[t]=[])).push({fn:e,ctx:n}),this},once:function(t,e,n){function o(){r.off(t,o),e.apply(n,arguments)}var r=this;return o._=e,this.on(t,o,n)},emit:function(t){var e=[].slice.call(arguments,1),n=((this.e||(this.e={}))[t]||[]).slice(),o=0,r=n.length;for(o;o<r;o++)n[o].fn.apply(n[o].ctx,e);return this},off:function(t,e){var n=this.e||(this.e={}),o=n[t],r=[];if(o&&e)for(var i=0,a=o.length;i<a;i++)o[i].fn!==e&&o[i].fn._!==e&&r.push(o[i]);return r.length?n[t]=r:delete n[t],this}},t.exports=n},function(t,e,n){var o,r,i;!function(a,c){r=[t,n(0),n(2),n(1)],o=c,void 0!==(i="function"==typeof o?o.apply(e,r):o)&&(t.exports=i)}(0,function(t,e,n,o){"use strict";function r(t){return t&&t.__esModule?t:{default:t}}function i(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function a(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function c(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}function u(t,e){var n="data-clipboard-"+t;if(e.hasAttribute(n))return e.getAttribute(n)}var l=r(e),s=r(n),f=r(o),d="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t},h=function(){function t(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}return function(e,n,o){return n&&t(e.prototype,n),o&&t(e,o),e}}(),p=function(t){function e(t,n){i(this,e);var o=a(this,(e.__proto__||Object.getPrototypeOf(e)).call(this));return o.resolveOptions(n),o.listenClick(t),o}return c(e,t),h(e,[{key:"resolveOptions",value:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};this.action="function"==typeof t.action?t.action:this.defaultAction,this.target="function"==typeof t.target?t.target:this.defaultTarget,this.text="function"==typeof t.text?t.text:this.defaultText,this.container="object"===d(t.container)?t.container:document.body}},{key:"listenClick",value:function(t){var e=this;this.listener=(0,f.default)(t,"click",function(t){return e.onClick(t)})}},{key:"onClick",value:function(t){var e=t.delegateTarget||t.currentTarget;this.clipboardAction&&(this.clipboardAction=null),this.clipboardAction=new l.default({action:this.action(e),target:this.target(e),text:this.text(e),container:this.container,trigger:e,emitter:this})}},{key:"defaultAction",value:function(t){return u("action",t)}},{key:"defaultTarget",value:function(t){var e=u("target",t);if(e)return document.querySelector(e)}},{key:"defaultText",value:function(t){return u("text",t)}},{key:"destroy",value:function(){this.listener.destroy(),this.clipboardAction&&(this.clipboardAction.destroy(),this.clipboardAction=null)}}],[{key:"isSupported",value:function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:["copy","cut"],e="string"==typeof t?[t]:t,n=!!document.queryCommandSupported;return e.forEach(function(t){n=n&&!!document.queryCommandSupported(t)}),n}}]),e}(s.default);t.exports=p})},function(t,e){function n(t,e){for(;t&&t.nodeType!==o;){if("function"==typeof t.matches&&t.matches(e))return t;t=t.parentNode}}var o=9;if("undefined"!=typeof Element&&!Element.prototype.matches){var r=Element.prototype;r.matches=r.matchesSelector||r.mozMatchesSelector||r.msMatchesSelector||r.oMatchesSelector||r.webkitMatchesSelector}t.exports=n},function(t,e,n){function o(t,e,n,o,r){var a=i.apply(this,arguments);return t.addEventListener(n,a,r),{destroy:function(){t.removeEventListener(n,a,r)}}}function r(t,e,n,r,i){return"function"==typeof t.addEventListener?o.apply(null,arguments):"function"==typeof n?o.bind(null,document).apply(null,arguments):("string"==typeof t&&(t=document.querySelectorAll(t)),Array.prototype.map.call(t,function(t){return o(t,e,n,r,i)}))}function i(t,e,n,o){return function(n){n.delegateTarget=a(n.target,e),n.delegateTarget&&o.call(t,n)}}var a=n(4);t.exports=r},function(t,e){e.node=function(t){return void 0!==t&&t instanceof HTMLElement&&1===t.nodeType},e.nodeList=function(t){var n=Object.prototype.toString.call(t);return void 0!==t&&("[object NodeList]"===n||"[object HTMLCollection]"===n)&&"length"in t&&(0===t.length||e.node(t[0]))},e.string=function(t){return"string"==typeof t||t instanceof String},e.fn=function(t){return"[object Function]"===Object.prototype.toString.call(t)}},function(t,e){function n(t){var e;if("SELECT"===t.nodeName)t.focus(),e=t.value;else if("INPUT"===t.nodeName||"TEXTAREA"===t.nodeName){var n=t.hasAttribute("readonly");n||t.setAttribute("readonly",""),t.select(),t.setSelectionRange(0,t.value.length),n||t.removeAttribute("readonly"),e=t.value}else{t.hasAttribute("contenteditable")&&t.focus();var o=window.getSelection(),r=document.createRange();r.selectNodeContents(t),o.removeAllRanges(),o.addRange(r),e=o.toString()}return e}t.exports=n}])});

const messages = {
  'en': {
    'copy': 'Copy',
    'copy_to_clipboard': 'Copy to clipboard',
    'copy_success': 'Copied to clipboard!',
    'copy_failure': 'Failed to copy',
  },
  'es' : {
    'copy': 'Copiar',
    'copy_to_clipboard': 'Copiar al portapapeles',
    'copy_success': '¡Copiado!',
    'copy_failure': 'Error al copiar',
  },
  'de' : {
    'copy': 'Kopieren',
    'copy_to_clipboard': 'In die Zwischenablage kopieren',
    'copy_success': 'Kopiert!',
    'copy_failure': 'Fehler beim Kopieren',
  }
}

let locale = 'en'
if( document.documentElement.lang !== undefined
    && messages[document.documentElement.lang] !== undefined ) {
  locale = document.documentElement.lang
}

/**
 * Set up copy/paste for code blocks
 */

const runWhenDOMLoaded = cb => {
  if (document.readyState != 'loading') {
    cb()
  } else if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', cb)
  } else {
    document.attachEvent('onreadystatechange', function() {
      if (document.readyState == 'complete') cb()
    })
  }
}

const codeCellId = index => `codecell${index}`

// Clears selected text since ClipboardJS will select the text when copying
const clearSelection = () => {
  if (window.getSelection) {
    window.getSelection().removeAllRanges()
  } else if (document.selection) {
    document.selection.empty()
  }
}

// Changes tooltip text for two seconds, then changes it back
const temporarilyChangeTooltip = (el, newText) => {
  const oldText = el.getAttribute('data-tooltip')
  el.setAttribute('data-tooltip', newText)
  setTimeout(() => el.setAttribute('data-tooltip', oldText), 2000)
}

const addCopyButtonToCodeCells = () => {
  // If ClipboardJS hasn't loaded, wait a bit and try again. This
  // happens because we load ClipboardJS asynchronously.
  if (window.ClipboardJS === undefined) {
    setTimeout(addCopyButtonToCodeCells, 250)
    return
  }

  const codeCells = document.querySelectorAll('div.highlight-default:not(.output) pre, div.highlight-bash pre, div.highlight-sh pre, div.highlight-python pre')
  codeCells.forEach((codeCell, index) => {
    const id = codeCellId(index)
    codeCell.setAttribute('id', id)
    const pre_bg = getComputedStyle(codeCell).backgroundColor;

    const clipboardButton = id =>
    `<a class="copybtn o-tooltip--left" data-tooltip="${messages[locale]['copy']}" data-clipboard-target="#${id}">
      <img src="https://raw.githubusercontent.com/choldgraf/sphinx-copybutton/master/sphinx_copybutton/_static/copy-button.svg" alt="${messages[locale]['copy_to_clipboard']}">
    </a>`
    codeCell.insertAdjacentHTML('afterend', clipboardButton(id))
  })

  const clipboard = new ClipboardJS('.copybtn')
  clipboard.on('success', event => {
    clearSelection()
    temporarilyChangeTooltip(event.trigger, messages[locale]['copy_success'])
  })

  clipboard.on('error', event => {
    temporarilyChangeTooltip(event.trigger, messages[locale]['copy_failure'])
  })
}

runWhenDOMLoaded(addCopyButtonToCodeCells);
"""

limit_output_length_css = r"""
pre.output {
  max-height: 400px;
  overflow-y: scroll;
}
div[class^="output"] {
    margin-bottom: 1em;
}
"""

tabbar_css = r"""
div.mdl-tabs__tab-bar { justify-content: left; }

.mdl-tabs .mdl-tabs__tab {
    font-size: 13px;
    height: 32px;
    line-height: 32px;
    border-radius: 4px 4px 0 0;
    letter-spacing: .5px;
}

.mdl-tabs .mdl-tabs__tab-bar {
    height: 32px;
}

.mdl-tabs .mdl-tabs__tab-bar.text {
    margin-bottom: .5em;
}

.mdl-tabs .mdl-tabs__tab-bar.code {
    margin-bottom: -1em;
}

.mdl-tabs__tab.is-active {
    background: rgb(0,0,0,.09);
}
"""

copybutton_css = r"""
a.copybtn {
    position: absolute;
    top: 12px;
    right: 24px;
    width: 1.2em;
    height: 1.2em;
    padding: 0 0 0 10px;
    opacity: .4;
    transition: opacity 0.5s;
    background-color: rgba(0, 0, 0, 0.02);
}

div.highlight  {
    position: relative;
}

.highlight:hover .copybtn {
	opacity: 1;
}

.o-tooltip--left {
    position: relative;
}

.o-tooltip--left:after {
    opacity: 0;
    visibility: hidden;
    position: absolute;
    content: attr(data-tooltip);
    padding: 2px 10px;
    top: -2px;
    left: 0;
    background: #666;
    font-size: 1rem;
    color: white;
    white-space: nowrap;
    z-index: 2;
    border-radius: 2px;
    transform: translateX(-102%) translateY(0);
    transition: opacity 0.2s cubic-bezier(0.64, 0.09, 0.08, 1), transform 0.2s cubic-bezier(0.64, 0.09, 0.08, 1);
}

.o-tooltip--left:hover:after {
    display: block;
    opacity: 1;
    visibility: visible;
    transform: translateX(-100%) translateY(0);
    transition: opacity 0.2s cubic-bezier(0.64, 0.09, 0.08, 1), transform 0.2s cubic-bezier(0.64, 0.09, 0.08, 1);
}
"""
