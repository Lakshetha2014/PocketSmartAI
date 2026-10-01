from flask import Flask
from routes.home import home_bp
from routes.planners import planner_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(planner_bp)


if __name__ == "__main__":
    app.run(debug=True)