"""GeoServer Manifest Previewer."""

import json

from flask import render_template
from invenio_i18n import gettext as _
from invenio_previewer.proxies import current_previewer
from invenio_previewer.utils import detect_encoding

previewable_extensions = ["json"]


def can_preview(file):
    """Check if file can be previewed."""
    return file.is_local() and file.has_extensions(".json")


def preview(file):
    """Render WMS from a JSON-LD file."""
    with file.open() as fp:
        encoding = detect_encoding(fp, default="utf-8")
        file_content = fp.read().decode(encoding)
        data = json.loads(file_content)

        wms_service = data.get("wmsService", {})
        base_url = wms_service.get("url")
        layer_name = wms_service.get("layerName")

        return render_template(
            "invenio_previewer_geoserver/geoserver.html",
            file=file,
            base_url=base_url,
            layer_name=layer_name,
            js_bundles=current_previewer.js_bundles + ["geoserver_js.js"],
            css_bundles=current_previewer.css_bundles + ["geoserver_css.css"],
        )
