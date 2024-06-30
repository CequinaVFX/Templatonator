import nuke
from main import Templatonator

toolbar = nuke.menu('Nodes')
pythonTools = toolbar.addMenu('Templatonator')
pythonTools.addCommand('Templatonator',
                       'Templatonator().collect_data()')


"""
['paste template',
'script read',
'save to script',
'open template',
'copy as text',]

"""