from flask import Flask

# You can import home directly from the routes package, because its __init__.py file imported (and renamed) the blueprint. 
# Otherwise, you'd have to add from app.routes.home import bp as home and then repeat that line for any new modules that you added to routes
# from app.routes import home

from app.routes import home, dashboard

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

# Thats the JS version
# Flask is like Express.js
#   app.get('/hello', (req, res) => {
#  res.send('hello world');
# });
  @app.route('/hello')
  def hello():
    return 'hello world'

  # register routes
  # register the dashboard routes alongside the homepage routes
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  return app
