# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 CERN.
#
# Invenio-Previewer-GeoServer is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Invenio module that adds more fun to the platform."""

from flask import Blueprint, render_template

blueprint = Blueprint(
    "invenio_previewer_geoserver",
    __name__,
    template_folder="templates",
    static_folder="static",
)
