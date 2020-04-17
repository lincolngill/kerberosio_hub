#!/usr/bin/env python3
from khub import db
from khub.models import User, CameraGroup, Camera

db.drop_all()
db.create_all()

db.session.add(User(username='links', email='lincolngill@gmail.com', password='l00king'))

cg = CameraGroup(name='Home', dashboard_route='/home')
db.session.add(cg)
cg = CameraGroup.query.filter_by(name='Home').first()

db.session.add(Camera(name='Camera 1', location='Rumpus Room', url='http://192.168.1.61:8889/', group_id=cg.id))
db.session.add(Camera(name='Camera 2', location='Front Entrance', url='http://192.168.1.6:8889/', group_id=cg.id))

db.session.commit()

print(User.query.first())
cg = CameraGroup.query.filter_by(name='Home').first()
print(cg)
for c in cg.cameras:
    print(c)