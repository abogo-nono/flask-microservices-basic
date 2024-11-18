from flask import Flask, request, jsonify

from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = '123456890'
jwt = JWTManager(app)

@app.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()

    return jsonify({
        'user': current_user
    }, 200)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
