from flask import Flask, request, jsonify
from routes.auth import auth_bp
from utils.error_handler import register_error_handler
app = Flask(__name__)

app.config.from_object("config.Config")

register_error_handler(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route("/health")
def home():
    return jsonify({"success": "Flask chal raha hai"})

# query params
# example -> /search?name=fujel&age=25
# use -->They are used to identify a specific resource.
@app.route("/search")
def search():
    name= request.args.get("name")
    age= request.args.get("age")

    return jsonify({
        "name": name,
        "age": age
    })

# URL params
# use -->They are used to filter, sort, or search data.
@app.route("/user/<username>")
def user(username):
    return jsonify({
        "user": username
    })

# post request

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)