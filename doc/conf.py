# -*- coding: utf-8 -*-
import sys
import os
import glob
import shutil
import datetime
import sphinx_rtd_theme
import sphinx_gallery
from sphinx_gallery.sorting import FileNameSortKey, ExplicitOrder
from pygmt import __version__, __commit__
from pygmt.sphinx_gallery import PyGMTScraper


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "nbsphinx",
    "sphinx_gallery.gen_gallery",
]

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = False

numpydoc_class_members_toctree = False

# intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", None),
    "xarray": ("http://xarray.pydata.org/en/stable/", None),
}

sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": [
        "../examples/gallery",
        "../examples/tutorials",
        "../examples/projections",
    ],
    # path where to save gallery generated examples
    "gallery_dirs": ["gallery", "tutorials", "projections"],
    "subsection_order": ExplicitOrder(
        ["../examples/gallery/coast", "../examples/gallery/plot"]
    ),
    # Patter to search for example files
    "filename_pattern": r"\.py",
    # Remove the "Download all examples" button from the top level gallery
    "download_all_examples": False,
    # Sort gallery example by file name instead of number of lines (default)
    "within_subsection_order": FileNameSortKey,
    # directory where function granular galleries are stored
    "backreferences_dir": "api/generated/backreferences",
    # Modules for which function level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    "doc_module": "pygmt",
    # Insert links to documentation of objects in the examples
    "reference_url": {"pygmt": None},
    "image_scrapers": (PyGMTScraper(),),
}

# Sphinx project configuration
templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
source_suffix = ".rst"
# The encoding of source files.
source_encoding = "utf-8-sig"
master_doc = "index"

# General information about the project
year = datetime.date.today().year
project = "PyGMT"
copyright = "2017-{}, The PyGMT Developers.".format(year)
if len(__version__.split("+")) > 1 or __version__ == "unknown":
    version = "dev"
else:
    version = __version__

# These enable substitutions using |variable| in the rst files
rst_epilog = """
.. |year| replace:: {year}
""".format(
    year=year
)

html_last_updated_fmt = "%b %d, %Y"
html_title = "PyGMT"
html_short_title = "PyGMT"
html_logo = ""
html_favicon = "_static/favicon.png"
html_static_path = ["_static"]
html_extra_path = []
pygments_style = "default"
add_function_parentheses = False
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

# Theme config
html_theme = "sphinx_rtd_theme"
html_theme_options = {}
html_context = {
    "menu_links": [
        (
            '<i class="fa fa-users fa-fw"></i> Contributing',
            "https://github.com/GenericMappingTools/pygmt/blob/master/CONTRIBUTING.md",
        ),
        (
            '<i class="fa fa-gavel fa-fw"></i> Code of Conduct',
            "https://github.com/GenericMappingTools/pygmt/blob/master/CODE_OF_CONDUCT.md",
        ),
        (
            '<i class="fa fa-book fa-fw"></i> License',
            "https://github.com/GenericMappingTools/pygmt/blob/master/LICENSE.txt",
        ),
        (
            '<i class="fa fa-comment fa-fw"></i> Contact',
            "https://gitter.im/GenericMappingTools/pygmt",
        ),
        (
            '<i class="fa fa-github fa-fw"></i> Source Code',
            "https://github.com/GenericMappingTools/pygmt",
        ),
    ],
    # Custom variables to enable "Improve this page"" and "Download notebook"
    # links
    "doc_path": "doc",
    "galleries": sphinx_gallery_conf["gallery_dirs"],
    "gallery_dir": dict(
        zip(sphinx_gallery_conf["gallery_dirs"], sphinx_gallery_conf["examples_dirs"])
    ),
    "github_repo": "GenericMappingTools/pygmt",
    "github_version": "master",
}


# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
