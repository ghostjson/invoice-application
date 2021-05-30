import eel

from database import *


@eel.expose
def test():
	print('working')


eel.init('ui')
eel.start('invoices.html', size=(1000, 600))