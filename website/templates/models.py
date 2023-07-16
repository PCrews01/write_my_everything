from website import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer)
    first_name = db.Column(db.String(10))
    last_name = db.Column(db.String(10))
    email = db.Column(db.String(60))
    school = db.ForeignKey('schools.id')
    grade = db.Column(db.String)
    essays = db.ForeignKey('essays.id')
    premium = db.Column(db.Boolean, default=False)
    
class Schools(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(60))
    student_count = db.Column(db.Integer)
    domain = db.Column(db.String(60))    
    
class Essays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(50))
    essay = db.Column(db.String)
    topic = db.Column(db.String(50))
    grade_level = db.Column(db.String(10))
    essay_measurement = db.Column(db.String)
    essay_length = db.Column(db.Integer)
    spell_check = db.Column(db.Boolean, default=False)
    grammar_check = db.Column(db.Boolean, default=False)
    outline = db.Column(db.Boolean, default=False)
    prompt = db.Column(db.String)
    
class Topics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(50))
    uses = db.Column(db.Integer)