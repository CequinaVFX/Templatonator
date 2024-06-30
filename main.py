import os
from datetime import datetime

import nuke
import nukescripts


def save_path():
    return '/'.join([os.path.dirname(__file__), 'save_template'])


def save_filename(template):
    save_file = r'{}_{}'.format(template, datetime.now().strftime("%b_%d_%H_%M_%S"))
    save_at = save_path()

    if not os.path.isdir(save_at):
        try:
            os.mkdir(save_at)
        except SystemError as error:
            print(error)

    return '/'.join([save_at, '{}.nk'.format(save_file)])


def get_templates_folder():
    return '/'.join([os.path.dirname(__file__), 'templates'])


def get_template_file(template):
    folder = get_templates_folder()
    template_file = '/'.join([folder, '{}.nk'.format(template)])

    if os.path.isfile(template_file):
        return template_file

    return


def get_templates_files():
    templates_folder = get_templates_folder()
    templates = ['none              ']

    if os.path.isdir(templates_folder):
        for _a_, _b_, _templates in os.walk(templates_folder):
            for file in _templates:
                if file.endswith('nk'):
                    templates.append(file.replace('.nk', ''))
                else:
                    pass

    return templates


class Templatonator:
    def __init__(self):
        self.template_file = None
        self.save_filename = None

    def collect_data(self):
        temp = TemplatonatorUI()
        data = temp.get_data()

        self.template_file = get_template_file(template=data['template'])
        self.save_filename = save_filename(template=data['template'])

        mode = data['mode']

    def paste_template(self):
        """
        https://learn.foundry.com/nuke/developers/140/pythonreference/_autosummary/nuke.nodePaste.html
        nuke.nodePaste(s)> Node
        or
        https://learn.foundry.com/nuke/developers/140/pythonreference/_autosummary/nuke.loadToolset.html
        nuke.loadToolset(filename=None, overwrite=- 1)> None

        :pros: no errors
        :cons: do not load color management from template

        """
        # insert the template nodes into the current script
        nuke.nodePaste(self.template_file)

        # save scripts as
        nuke.scriptSaveAs(self.save_filename)

    def script_read(self):
        """
        https://learn.foundry.com/nuke/developers/140/pythonreference/_autosummary/nuke.scriptReadFile.html
        nuke.scriptReadFile()
        or
        https://learn.foundry.com/nuke/developers/140/pythonreference/_autosummary/nuke.scriptSource.html
        nuke.scriptSource()

        :pros: load color management from template
        """
        # load the template content to the current script
        nuke.scriptReadFile(self.template_file)

        # save scripts as
        nuke.scriptSaveAs(self.save_filename)


    def save_to_script(self):
        """
        nuke.saveToScript(filename, fileContent)> None
        """
        pass


    def open_template(self):
        pass

    def copy_as_text(self):
        with open(self.template_file, 'r+') as read_original:
            template_content = read_original.read()

        with open(self.save_filename, 'w+') as open_destination:
            open_destination.write(template_content)


class TemplatonatorUI(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Templatonator')

        self.spc00 = nuke.Text_Knob('spc00', '', ' ')
        self.addKnob(self.spc00)

        valid_templates = get_templates_files()

        self.template_knob = nuke.Enumeration_Knob('template_name', 'template name', valid_templates)
        self.template_knob.clearFlag(nuke.STARTLINE)
        self.addKnob(self.template_knob)

        self.spc10 = nuke.Text_Knob('spc10', '', ' ')
        self.addKnob(self.spc10)

        self.mode_knob = nuke.Enumeration_Knob('mode', 'mode', ['Load Template',
                                                                'Open template',
                                                                'Script read',
                                                                'Copy as text',
                                                                'Terminal command'])
        self.addKnob(self.mode_knob)

        self.spc30 = nuke.Text_Knob('spc30', '', ' ')
        self.addKnob(self.spc30)

        self.spc40 = nuke.Text_Knob('spc40', '', ' ')
        self.addKnob(self.spc40)

    def get_data(self):
        self.setMinimumSize(400, 200)
        result = self.showModalDialog()

        if result:
            data = {'template' : self.template_knob.value(),
                    'mode' : self.mode_knob.value()
                    }
            return data


def run():
    template = Templatonator()
    template.collect_data()


if __name__ == '__main__':
    run()
