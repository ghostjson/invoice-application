import eel

from database import *
from export import *

@eel.expose
def test():
	print('working')


eel.init('ui')
eel.start('login.html',size=(1000, 600))