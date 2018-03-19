import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT=os.path.join(BASE_DIR,"static")
STATICFILES_DIRS =os.path.join(os.path.dirname(__file__),"static")
BASE1_DIR=os.path.join(BASE_DIR,"mvit")
print(BASE1_DIR)
print(STATIC_ROOT)
