from app import app, db
from app.models import NomineeLookup, CategoryLookup, RottenTomatoes, CategoryNominee, AwardLookup, AwardWinner, AppUser, Pick

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'NomineeLookup': NomineeLookup, 'CategoryLookup': CategoryLookup, 'RottenTomatoes': RottenTomatoes, 'CategoryNominee': CategoryNominee, 'AwardLookup': AwardLookup, 'AwardWinner': AwardWinner, 'AppUser': AppUser, 'Pick': Pick}
