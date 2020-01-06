from app.api import bp
from app.models import User
from flask import jsonify
from app.api.errors import bad_request
from app import db
from flask import url_for, request
@bp.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    return jsonify(User.query.filter_by(username=username).first_or_404().user_to_dict())

@bp.route('/users', methods=['GET'])
def get_users():
    pass

@bp.route('/users/<string:username>/connections', methods=['GET'])
def get_followers(id):
    pass

@bp.route('/users/<string:username>/followed', methods=['GET'])
def get_followed(id):
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    print(data)
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request("Must include username, password, and email")
    if User.query.filter_by(username=data['username']).first():
        return bad_request("Username already exists")
    if User.query.filter_by(email=data['email']).first():
        return bad_request("Email already exists")

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.user_to_dict())
    response.status_code = 201 
    response.headers['Location'] = url_for('api.get_user', username=user.username)
    return response
    


@bp.route('/users/<string:username>', methods=['PUT'])
def update_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and User.query.filter_by(username=data['username']).first():
        return bad_request('please change username')
    if 'email' in data and data['email'] != user.email and User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.user_to_dict())