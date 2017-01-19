'''
Created on 16 Nov 2016

@author: gbstring
'''
import os
from app import create_app, db
from app.models import Title, Person
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
#from config import Config

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, Title=Title, Person=Person)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



if __name__ == '__main__':
    manager.run()