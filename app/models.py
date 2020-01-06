from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



connections = db.Table('connections',
    db.Column('user_a_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('user_b_id', db.Integer, db.ForeignKey('user.id'))
)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    about_me = db.Column(db.String(150))
    name = db.Column(db.String(64))
    year = db.Column(db.String(64))
    major = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    connected = db.relationship(
        'User', secondary=connections,
        primaryjoin=(connections.c.user_a_id == id),
        secondaryjoin=(connections.c.user_b_id == id),
        backref=db.backref('connections', lazy='dynamic'), lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def connect(self, user):
        if not self.is_connected(user):
            self.connected.append(user)
    
    def disconnect(self, user):
        if self.is_connected(user):
            self.connected.remove(user)

    def is_connected(self, user):
        return self.connected.filter(connections.c.user_b_id==user.id).count() >0

    def user_to_dict(self, include_email=False):
        user_data = {
            'id': self.id,
            'username': self.username,
            'about_me': self.about_me,
            'post_count': self.posts.count(),
            'connection_count': self.connections.count(),
            # '_links': {
            #     'self': url_for('api.get_user', id=self.id),
            #     # 'connections': url_for('api.get_connections', id=self.id),
            # }
        }
        return user_data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

            
    def __repr__(self):
        return "<User {}>".format(self.username)




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Post {}>".format(self.body)

