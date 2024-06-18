from aiohttp import web
from aiohttp_utils import run
from app import create_app

if __name__ == "__main__":
    app = create_app()
    run(app, app_uri="app:create_app()", host="0.0.0.0", reload=True)
