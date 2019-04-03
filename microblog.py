from app import app, db                # note two tokens of 'app' are diff vars
from app.models import User, Post      # the first is the package, the second is
                                       # the var created in the __init__.py file
app.config["DEBUG"] = True

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
