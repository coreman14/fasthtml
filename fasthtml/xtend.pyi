__all__ = ['picocss', 'picolink', 'picocondcss', 'picocondlink', 'set_pico_cls', 'Html', 'A', 'AX', 'Checkbox', 'Card', 'Group', 'Search', 'Grid', 'DialogX', 'Hidden', 'Container', 'Script', 'Style', 'double_braces', 'undouble_braces', 'loose_format', 'ScriptX', 'replace_css_vars', 'StyleX', 'run_js', 'Titled', 'jsd']
from dataclasses import dataclass, asdict
from fastcore.utils import *
from fastcore.xtras import partial_format
from fastcore.xml import *
from fastcore.meta import use_kwargs, delegates
from .components import *
try:
    from IPython import display
except ImportError:
    display = None
picocss = 'https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.min.css'
picolink = (Link(rel='stylesheet', href=picocss), Style(':root { --pico-font-size: 100%; }'))
picocondcss = 'https://cdn.jsdelivr.net/npm/@picocss/pico@latest/css/pico.conditional.min.css'
picocondlink = (Link(rel='stylesheet', href=picocondcss), Style(':root { --pico-font-size: 100%; }'))

def set_pico_cls():
    ...

def Html(*c, doctype=True, **kwargs) -> XT:
    """An HTML tag, optionally preceeded by `!DOCTYPE HTML`"""
    ...

def A(*c, hx_get=None, target_id=None, hx_swap=None, href='#', id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """An A tag; `href` defaults to '#' for more concise use with HTMX"""
    ...

def AX(txt, hx_get=None, target_id=None, hx_swap=None, href='#', *, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """An A tag with just one text child, allowing hx_get, target_id, and hx_swap to be positional params"""
    ...

def Checkbox(checked: bool=False, label=None, value='1', *, target_id=None, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A Checkbox optionally inside a Label"""
    ...

def Card(*c, header=None, footer=None, target_id=None, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A PicoCSS Card, implemented as an Article with optional Header and Footer"""
    ...

def Group(*c, target_id=None, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A PicoCSS Group, implemented as a Fieldset with role 'group'"""
    ...

def Search(*c, target_id=None, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A PicoCSS Search, implemented as a Form with role 'search'"""
    ...

def Grid(*c, cls='grid', target_id=None, id=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A PicoCSS Grid, implemented as child Divs in a Div with class 'grid'"""
    ...

def DialogX(*c, open=None, header=None, footer=None, id=None, target_id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A PicoCSS Dialog, with children inside a Card"""
    ...

def Hidden(value: str='', *, target_id=None, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """An Input of type 'hidden'"""
    ...

def Container(*args, target_id=None, id=None, cls=None, title=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """A PicoCSS Container, implemented as a Main with class 'container'"""
    ...

def Script(code: str='', *, id=None, cls=None, title=None, style=None, **kwargs) -> XT:
    """A Script tag that doesn't escape its code"""
    ...

def Style(*c, id=None, cls=None, title=None, style=None, **kwargs) -> XT:
    """A Style tag that doesn't escape its code"""
    ...

def double_braces(s):
    """Convert single braces to double braces if next to special chars or newline"""
    ...

def undouble_braces(s):
    """Convert double braces to single braces if next to special chars or newline"""
    ...

def loose_format(s, **kw):
    """String format `s` using `kw`, without being strict about braces outside of template params"""
    ...

def ScriptX(fname, type=None, _async=None, defer=None, charset=None, crossorigin=None, integrity=None, **kw):
    """Create a Script from the text of a file"""
    ...

def replace_css_vars(css, pre='tpl', **kwargs):
    ...

def StyleX(fname, **kw):
    ...

def run_js(js, id=None, **kw):
    """Run `js` script, auto-generating `id` based on name of caller if needed, and js-escaping any `kw` params"""
    ...

def Titled(title: str='FastHTML app', *args, target_id=None, id=None, cls=None, style=None, accesskey=None, contenteditable=None, dir=None, draggable=None, enterkeyhint=None, hidden=None, inert=None, inputmode=None, lang=None, popover=None, spellcheck=None, tabindex=None, translate=None, hx_get=None, hx_post=None, hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None, hx_swap=None, hx_include=None, hx_select=None, hx_indicator=None, hx_push_url=None, hx_confirm=None, hx_disable=None, hx_replace_url=None, hx_on=None, **kwargs) -> XT:
    """An HTML partial containing a `Title`, and `H1`, and any provided children"""
    ...

def jsd(org, repo, root, path, prov='gh', typ='script', ver=None, esm=False, **kwargs) -> XT:
    """jsdelivr `Script` or CSS `Link` tag, or URL"""
    ...