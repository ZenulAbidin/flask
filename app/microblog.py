from app import app, db
from app.models import User, Post
from flask import url_for

if __name__ == "__main__":
    app.run()
    app.add_url_rule('/favicon.ico',
                     redirect_to=url_for('static', filename='favicon.ico'))


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
