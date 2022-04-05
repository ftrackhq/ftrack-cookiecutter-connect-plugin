# :coding: utf-8
# :copyright: Copyright (c) 2014 ftrack

import os
import sys
import logging
logger = logging.getLogger('ftrack-connect.widget.{{cookiecutter.widget_name}}')

cwd = os.path.dirname(__file__)
sources = os.path.abspath(os.path.join(cwd, '..', 'dependencies'))
sys.path.append(sources)

import platform
import ftrack_api
from ftrack_connect.qt import QtWidgets, QtCore, QtGui
import qtawesome as qta
import ftrack_connect.ui.application


class {{cookiecutter.widget_name}}(ftrack_connect.ui.application.ConnectWidget):
    name = '{{cookiecutter.widget_name}}'

    def __init__(self, session, parent=None):
        '''Instantiate the actions widget.'''
        super({{cookiecutter.widget_name}}, self).__init__(session, parent=parent)



def register(session, **kw):
    '''Register plugin. Called when used as an plugin.'''
    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an old or incompatible API and
    # return without doing anything.
    if not isinstance(session, ftrack_api.session.Session):
        logger.debug(
            'Not subscribing plugin as passed argument {0!r} is not an '
            'ftrack_api.Session instance.'.format(session)
        )
        return

    #  Uncomment to register plugin
    plugin = ftrack_connect.ui.application.ConnectWidgetPlugin({{cookiecutter.widget_name}})
    plugin.register(session, priority=50)