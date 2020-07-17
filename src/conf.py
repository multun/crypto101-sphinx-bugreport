#!/usr/bin/env python3
# -*- coding: utf-8 -*-

extensions = []

# only parse rst files
source_suffix = ".rst"

# paths to exclude from the document source scan
exclude_patterns = ["_release", "_build", "_build_*", "Thumbs.db", ".DS_Store", ".venv"]

# the name of the root document
master_doc = "index"

# i18n configuration
locale_dirs = ["locale/"]
gettext_compact = False

pygments_style = "sphinx"
