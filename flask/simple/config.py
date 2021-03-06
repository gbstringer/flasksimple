'''
Created on 16 Nov 2016

@author: gbstring
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dskc8dfwer74gfrhg47rjhhwr8743hgrfr9rwthwkt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    

    @staticmethod
    def init_app(app):
        pass   
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data', 'data-dev.sqlite')
    
class ProductionConfig(Config):
    '''
    
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'data', 'data.sqlite')
        
config =  {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    
    'default': DevelopmentConfig
    }   