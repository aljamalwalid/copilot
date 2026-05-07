import json
from pathlib import Path

from jupyter_server.base.handlers import APIHandler
import tornado

_STATIC_DIR = Path(__file__).resolve().parent / "static"


class ClouderaCopilotAvatarHandler(APIHandler):
    """Serves ``cloudera-copilot.svg`` at ``/api/ai/static/cloudera-copilot.svg`` for magics persona URLs."""

    @tornado.web.authenticated
    def get(self):
        path = _STATIC_DIR / "cloudera-copilot.svg"
        if not path.is_file():
            raise tornado.web.HTTPError(404, reason="Cloudera Copilot avatar not found")
        self.set_header("Content-Type", "image/svg+xml; charset=utf-8")
        self.set_header("Cache-Control", "public, max-age=86400")
        self.write(path.read_text(encoding="utf-8"))


class RouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            "data": "This is /api/jupyternaut/get-example endpoint!"
        }))

