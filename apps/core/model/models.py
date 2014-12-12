# -*- coding:utf-8 -*-
from apps import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    joinDATE = db.Column(db.DateTime(),default = db.func.now())

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.LargeBinary)
    category =db.Column(db.String(255))
    score = db.Column(db.Integer, default =1)
    count = db.Column(db.Integer, default = 1)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image = db.Column(db.LargeBinary)
    category = db.Column(db.String(255))
    #노모가 0, 유모가 1
    exposure = db.Column(db.Integer, default=1)
    score = db.Column(db.Integer, default=1)
    count = db.Column(db.Integer, default=1)

class ActorReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('actorReview', cascade='all, delete-orphan', lazy='dynamic'))
    actorID = db.Column(db.Integer, db.ForeignKey(Actor.id))
    user = db.relationship('User', backref=db.backref('actorReview', cascade='all, delete-orphan', lazy='dynamic'))
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    content = db.Column(db.Text())
    created=db.Column(db.DateTime(), default=db.func.now())

class VideoReview(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('videoReview', cascade='all, delete-orphan', lazy='dynamic'))
    videoID = db.Column(db.String(255), db.ForeignKey(Video.id))
    user = db.relationship('User', backref=db.backref('videoReview', cascade='all, delete-orphan', lazy='dynamic'))
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    content = db.Column(db.Text())
    created=db.Column(db.DateTime(), default=db.func.now())

class Filmo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    actor = db.relationship('Actor', backref=db.backref('Filmo', cascade='all, delete-orphan', lazy='dynamic'))
    video = db.relationship('Video', backref=db.backref('Filmo', cascade='all, delete-orphan', lazy='dynamic'))
    videoID = db.Column(db.Integer, db.ForeignKey(Video.id))
    ActorID = db.Column(db.Integer, db.ForeignKey(Actor.id))

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    video = db.relationship('Video', backref=db.backref('rating', cascade='all, delete-orphan', lazy='dynamic'))
    videoID = db.Column(db.Integer, db.ForeignKey(Video.id))
    user = db.relationship('User', backref=db.backref('rating', cascade='all, delete-orphan', lazy='dynamic'))
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    rating = db.Column(db.Integer, default=0)

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user = db.relationship('User', backref=db.backref('favorite', cascade='all, delete-orphan', lazy='dynamic'))
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    actor = db.relationship('Actor', backref=db.backref('favorite', cascade='all, delete-orphan', lazy='dynamic'))
    actorID = db.Column(db.Integer, db.ForeignKey(Actor.id))

class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video = db.relationship('Video', backref=db.backref('bookmark',cascade='all, delete-orphan',lazy='dynamic'))
    videoID=db.Column(db.Integer, db.ForeignKey(Video.id))
    user = db.relationship('User', backref=db.backref('bookmark',cascade='all, delete-orphan',lazy='dynamic'))
    userID=db.Column(db.Integer, db.ForeignKey(User.id))


