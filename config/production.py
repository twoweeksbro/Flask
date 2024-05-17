from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'S\\\xd5\x14\xc2\xb3Y6\xd4\xcc\xf2\x0f\x18\xcdZ\x0c'
