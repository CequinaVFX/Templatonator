import nuke
from main import Templatonator

toolbar = nuke.menu('Nodes')
pythonTools = toolbar.addMenu('Templatonator')
pythonTools.addCommand('Templatonator',
                       'Templatonator().collect_data()')


"""
['Paste template',
'Open template',
'Script read',
'Copy as text',
'Terminal command']

"""