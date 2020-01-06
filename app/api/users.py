from app.api import bp
from app.models import User
from flask import jsonify

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
    pass

@bp.route('/users/<string:username>', methods=['PUT'])
def update_user(id):
    pass