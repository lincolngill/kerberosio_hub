from khub import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    admin = db.Column(db.Boolean(), nullable=False, default=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class CameraGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    dashboard_route = db.Column(db.String(60), unique=True, nullable=False)
    cameras = db.relationship('Camera', backref='group', lazy=True)

    def __repr__(self):
        return f"CameraGroup('{self.name}', '{self.dashboard_route}')"

class Camera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    location = db.Column(db.String(60))
    url= db.Column(db.String(200), unique=True, nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('camera_group.id'), nullable=False)

    def __repr__(self):
        return f"Camera('{self.name}', '{self.location}', '{self.url}'"