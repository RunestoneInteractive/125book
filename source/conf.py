# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# Imports for runestone
import runestone
import pkg_resources  # to get runestone version

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('_exts'))

# -- Project information -----------------------------------------------------

project = 'CS/DS 125 Book (Title TBD)'
course_id = '125book'  # for Runestone
copyright = '2018, Mark Liffiton and Brad Sheese'
author = 'Mark Liffiton and Brad Sheese'
license_text = """
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png" /></a> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.  See <a href="/AB-License.html">License</a> for details.
"""

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax', 'sphinx.ext.todo']
extensions += ['runestone.common', 'runestone.activecode']
# Or:
#extensions += runestone.runestone_extensions()

# Add my extension
extensions += ['trinket']


# Enable todos
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for Runestone ---------------------------------------------------

# Class(es) assigned to activecode divs
# (Doesn't override the javascript's addition of alert and alert-warning to an
# inner div, though...)
activecode_div_class = "runestone explainer ac_section"

# `rst_prolog <http://www.sphinx-doc.org/en/stable/config.html#confval-rst_prolog>`_:
# A string of reStructuredText that will be included at the beginning of every
# source file that is read.
# For fill-in-the-blank questions, provide a convenient means to indicate a blank.
# 2018-06-25: Probably only works with the right runestone ext installed above...
#rst_prolog = ".. |blank| replace:: :blank:`x`"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_bootstrap'

# Tell it where to find the theme
html_theme_path = ["_templates/plugin_layouts"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navbar_site_name': "Chapters",
    'globaltoc_depth': 1,
    'source_link_position': "",  # Options: 'nav', 'footer', anything else to disable
}

# For Runestone
html_context = {
    'course_id': course_id,
    'login_required': 'false',
    'use_services': 'false',
    'python3': 'true',
    'downloads_enabled': 'true',
    'loglevel': 10,
    'license_text': license_text,
    'runestone_version': pkg_resources.require("runestone")[0].version,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static'] + runestone.runestone_static_dirs()

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = '125bookdoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, '125book.tex', '125book Documentation',
     'Mark Liffiton and Brad Sheese', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    #(master_doc, '125book', '125book Documentation',
    # [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    #(master_doc, '125book', '125book Documentation',
    # author, '125book', 'One line description of project.',
    # 'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
