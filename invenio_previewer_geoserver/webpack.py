"""JS/CSS Webpack bundles for Invenio Previewer GeoServer."""

from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "geoserver_js": "./js/invenio_previewer_geoserver/geoserver.js",
                "geoserver_css": "./css/invenio_previewer_geoserver/geoserver.css",
            },
            dependencies={
                "leaflet": "^1.9.4",
            },
        ),
    },
)
