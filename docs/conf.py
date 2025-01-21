# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys

# ONDERSTAANDE KOMT UIT openzaak 
# maar het pad ../src gaat naar de source van heel openzaak. 
# dus onderstaande gebruik ik maar niet. 
# import django
# sys.path.insert(0, os.path.abspath("../src"))

# onderstaande komt uit https://github.com/readthedocs/readthedocs.org/blob/main/docs/conf.py
# dus daarvan neem ik dan ook de map _ext over, met daarin alleen 
# readthedocs.org/docs/_ext/djangodocs.py

sys.path.append(os.path.abspath("_ext"))




# -- Project information -----------------------------------------------------

project = "KISS"
copyright = "2024"
# # author = objects.__author__

# The full version, including alpha/beta/rc tags
# # release = objects.__version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# Volgens mij heb ik iig nodig: sphinx_rtd_theme, én myst_parser (voor markdown)
# gekopieerd uit Openzaak: "sphinx.ext.todo","recommonmark","sphinx_markdown_tables","sphinx_tabs.tabs"

extensions = [
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinx.ext.todo",
]



# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "nl"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_logo = "logo.png"
html_theme = "sphinx_rtd_theme"

# onderstaande komt uit: 
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'style_nav_header_background': 'blue',
    'flyout_display': 'attached',
    'version_selector': True,
    'language_selector': True,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False   
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".


# ik weet niet zo goed waar deze vandaan komt. En ik heb dus wel een theme_override.css
# Ik weet niet helemaal wat die doet, maar ik ga m toch gebruiken. 
# ik zet deze comment boven html_static, omdat copilot dat suggereert. 

html_static_path = ["_static"]
html_css_files = [
    "theme_override.css",  # override wide tables with word wrap
]

# deze komt ook uit openzaak
# maar zij gebruiken gegenereerde content. dus deze gebruik ik ook niet
#
# todo_include_todos = True

