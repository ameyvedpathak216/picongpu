# -*- coding: utf-8 -*-
#
# PIConGPU documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 14 17:29:56 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys
python_libs = os.path.abspath('../../lib/python')
sys.path.insert(0, python_libs)

# for autodoc example
sys.path.insert(0, os.path.abspath("./pypicongpu"))


# -- General configuration ------------------------------------------------

# RTD
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

show_authors = True

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'breathe',
              'sphinxcontrib.programoutput',
              'matplotlib.sphinxext.plot_directive',
              'autoapi.extension',
              'myst_parser']

# enable latex physics package in math expressions
# https://docs.mathjax.org/en/v3.1-latest/input/tex/extensions/physics.html
mathjax3_config = {
    'loader': {'load': ['[tex]/physics']},
    'tex': {'packages': {'[+]': ['physics']}}}

if not on_rtd:
    extensions.append('sphinx.ext.githubpages')

# enable figure and table enumeration
numfig = True
# When set to True equations are numbered across the whole documentation.
# If False the numbering begins from 1 on each page.
math_numfig = False


# napoleon autodoc config
napoleon_include_init_with_doc = True
autodoc_mock_imports = [
    'h5py',
    'pandas',
    'ipywidgets',
    'ipympl',
]

# breathe config
breathe_projects = {'PIConGPU': '../xml'}
breathe_default_project = 'PIConGPU'

breathe_domain_by_extension = {
    "cu":       "cpp",
    "cpp":      "cpp",
    "kernel":   "cpp",
    "h":        "cpp",
    "hpp":      "cpp",
    "tpp":      "cpp",
    "def":      "cpp",
    "param":    "cpp",
    "unitless": "cpp",
    "loader":   "cpp"
}

if on_rtd:
    subprocess.call('cd ..; doxygen', shell=True)
else:
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'PIConGPU'
copyright = u'Documentation under CC-BY 4.0, The PIConGPU Community'
author = u'The PIConGPU Community'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.7.0'
# The full version, including alpha/beta/rc tags.
release = u'0.7.0-dev'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PIConGPUdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    'preamble': r'\setcounter{tocdepth}{2}',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'PIConGPU.tex', u'PIConGPU Documentation',
     u'The PIConGPU Community', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'picongpu', u'PIConGPU Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PIConGPU', u'PIConGPU Documentation',
     author, 'PIConGPU', 'A particle-in-cell code for GPGPU',
     """
     PIConGPU is a fully relativistic, many GPGPU, 3D3V particle-in-cell (PIC)
     code. The Particle-in-Cell algorithm is a central tool in plasma physics.
     It describes the dynamics of a plasma by computing the motion of electrons
     and ions in the plasma based on Maxwell's equations.
     """),
]


# sphinx autoapi configuration
autoapi_type = 'python'
autoapi_dirs = [
    python_libs + '/picongpu/pypicongpu',
]
autoapi_generate_api_docs = True
autoapi_options = ['members',
                   'inherited-members',
                   'undoc-members',
                   'special-members',
                   'show-inheritance',
                   'show-inheritance-diagram',
                   'show-module-summary',
                   'imported-members',
                   ]
autoapi_root = 'pypicongpu/autoapi'
# toctree entry is added manually
autoapi_add_toctree_entry = False
