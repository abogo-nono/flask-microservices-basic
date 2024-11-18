from flask import Flask, jsonify, request

from flask_jwt_extended import create_access_token, JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = '123456890'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('username')

    if username != 'test' and password != 'test':
        return jsonify({
            'message': 'Any user with this credentials'
        }, 401)

    access_token = create_access_token(identity=username)
    return jsonify({
        'access_token': access_token
    }, 201)


if __name__ == '__main__':
    app.run(debug=True, port=5000)