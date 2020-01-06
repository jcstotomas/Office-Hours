from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))


    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.connections.all(), [])

        u1.connect(u2)
        db.session.commit()
        self.assertTrue(u1.is_connected(u2))
        self.assertEqual(u1.connected.count(), 1)
        self.assertEqual(u1.connected.first().username, 'susan')
        self.assertEqual(u2.connections.count(), 1)
        self.assertEqual(u2.connections.first().username, 'john')

        u1.disconnect(u2)
        db.session.commit()
        self.assertFalse(u1.is_connected(u2))
        self.assertEqual(u1.connected.count(), 0)
        self.assertEqual(u2.connections.count(), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)