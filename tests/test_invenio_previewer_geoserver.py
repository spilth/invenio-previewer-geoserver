# -*- coding: utf-8 -*-
#
# Copyright (C) 2024 CERN.
#
# Invenio-Previewer-GeoServer is free software; you can redistribute it
# and/or modify it under the terms of the MIT License; see LICENSE file for
# more details.

"""Module tests."""

from flask import Flask

from invenio_previewer_geoserver import InvenioPreviewerGeoServer


def test_version():
    """Test version import."""
    from invenio_previewer_geoserver import __version__

    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask("testapp")
    ext = InvenioPreviewerGeoServer(app)
    assert "invenio-previewer-geoserver" in app.extensions

    app = Flask("testapp")
    ext = InvenioPreviewerGeoServer()
    assert "invenio-previewer-geoserver" not in app.extensions
    ext.init_app(app)
    assert "invenio-previewer-geoserver" in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert "Welcome to Invenio-Previewer-GeoServer" in str(res.data)
