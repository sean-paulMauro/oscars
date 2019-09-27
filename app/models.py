from app import db
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy_imageattach.entity import Image, image_attachment

#Base = declarative_base()

class NomineeLookup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True)
    #image = image_attachment('NomineePicture')
    year = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Nominee {}>'.format(self.name)
        
class CategoryLookup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    points = db.Column(db.Integer)
    notes = db.Column(db.String(2000))
    
    def __repr__(self):
        return '<Category {}>'.format(self.name)
        
class RottenTomatoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(500))
    consensus = db.Column(db.String(2000))
    score = db.Column(db.String(10))
    
    def __repr__(self):
        return '<RottenTomatoes {}>'.format(self.consensus)
        
class CategoryNominee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    odds = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category_lookup.id'))
    nominee_id = db.Column(db.Integer, db.ForeignKey('nominee_lookup.id'))
    rt_id = db.Column(db.Integer, db.ForeignKey('rotten_tomatoes.id'))
    
    def __repr__(self):
        return '<CategoryNominee {}>'.format(self.category_id + self.nominee_id)
        
class AwardLookup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), index=True, unique=True)
    boost = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category_lookup.id'))
    
    def __repr__(self):
        return '<AwardLookup {}>'.format(self.name)
        
class AwardWinner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_nominee_id = db.Column(db.Integer, db.ForeignKey('category_nominee.id'))    
    award_id = db.Column(db.Integer, db.ForeignKey('award_lookup.id'))
    
    def __repr__(self):
        return '<AwardWinner {}>'.format(self.category_nominee_id)
        
class AppUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    picks = db.relationship('Pick', backref='picker', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.email)
        
class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_nominee_id = db.Column(db.Integer, db.ForeignKey('category_nominee.id'))  
    app_user_id = db.Column(db.Integer, db.ForeignKey('app_user.id'))  
    
    def __repr__(self):
        return '<Pick {}>'.format(self.app_user_id + self.category_nominee_id)   
        
#class NomineePicture(Base, Image):
 #   id = db.Column(db.Integer, primary_key=True)
 #   nominee_id = db.Column(db.Integer, db.ForeignKey('nominee_lookup.id'))
    
    
