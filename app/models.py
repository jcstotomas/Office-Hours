from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import base64 
from datetime import datetime, timedelta
import os 


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
    interests = db.Column(db.String(256))
    skills_to_build = db.Column(db.String(256))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    connected = db.relationship(
        'User', secondary=connections,
        primaryjoin=(connections.c.user_a_id == id),
        secondaryjoin=(connections.c.user_b_id == id),
        backref=db.backref('connections', lazy='dynamic'), lazy='dynamic')
    token = db.Column(db.String(32), index=True, unique= True)
    token_expiration = db.Column(db.DateTime)


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
            'token': self.token,
            'skills_to_build': self.skills_to_build,
            "name": self.name,
            "interests": self.interests,
            "year": self.year,
            "major":self.major
            # '_links': {
            #     'self': url_for('api.get_user', id=self.id),
            #     # 'connections': url_for('api.get_connections', id=self.id),
            # }
        }
        return user_data

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if  self.token_expiration != None and (self.token and self.token_expiration > now + timedelta(seconds=60)):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me', 'interests', 'skills_to_build', 'year', 'name', 'major']:
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

