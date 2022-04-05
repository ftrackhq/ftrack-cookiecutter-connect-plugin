# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

import os
import sys
import logging
import functools
import platform
import ftrack_api
import ftrack_api.structure.standard
import ftrack_api.accessor.disk


dependencies_directory = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'dependencies')
)
sys.path.append(dependencies_directory)


# Pick the current folder location name.
this_dir = os.path.abspath(os.path.dirname(__file__))

from {{cookiecutter.package_name}}.accessor import {{cookiecutter.location_name}}Accessor
from {{cookiecutter.package_name}}.structure import {{cookiecutter.location_name}}Structure


mount_points = {
    'windows': 'P:\\ftrack\\projects',
    'linux': '/mnt/ftrack/projects',
    'darwin': '/mnt/ftrack/projects',
}

def configure_location(session, event):
    '''Configure locations for *session* and *event*.'''

    logging.info('Configuring location....')

    # Ensure environment variables options are available in event.
    if 'options' not in event['data']:
        event['data']['options'] = {'env': {}}

    environment = event['data']['options']['env']

    # Add this script path to the FTRACK_EVENT_PLUGIN_PATH.
    location_path = os.path.normpath(this_dir)
    environment['FTRACK_EVENT_PLUGIN_PATH'] = os.pathsep.join(
        [location_path, environment.get('FTRACK_EVENT_PLUGIN_PATH', '')]
    )
    
    mount_point = mount_points.get(platform.system().lower())
    if not os.path.exists(mount_point):
        raise IOError(f'{mount_point} not found.')

    structure = {{cookiecutter.location_name}}Structure()
    accessor = {{cookiecutter.location_name}}Accessor(mount_point)

    # Ensure new location.
    my_location = session.ensure('Location', {'name': structure.name})

    # ftrack_api.mixin(my_location, ftrack_api.entity.location.UnmanagedLocationMixin)

    # Set new structure in location.
    my_location.structure = structure

    # Set accessor.
    my_location.accessor = accessor

    # Set priority.
    my_location.priority = 30

    logging.info('Setting {} to {}'.format(structure, my_location))


def register(api_object):
    '''Register plugin with *api_object*.'''
    logger = logging.getLogger('ftrack-connect.location.register')

    # Validate that session is an instance of ftrack_api.Session. If not, assume
    # that register is being called from an old or incompatible API and return
    # without doing anything.
    if not isinstance(api_object, ftrack_api.Session):
        logger.debug(
            'Not subscribing plugin as passed argument {0} is not an '
            'ftrack_api.Session instance.'.format(api_object)
        )
        return

    # React to configure location event.
    api_object.event_hub.subscribe(
        'topic=ftrack.api.session.configure-location',
        functools.partial(configure_location, api_object),
        priority=0,
    )

    # React to application launch event.
    # This way the location will be available from within the integrations.
    api_object.event_hub.subscribe(
        'topic=ftrack.connect.application.launch',
        functools.partial(configure_location, api_object),
        priority=0,
    )

    # React to action launch event.
    # This way the location will be available from within the actions.
    api_object.event_hub.subscribe(
        'topic=ftrack.action.launch',
        functools.partial(configure_location, api_object),
        priority=0,
    )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # Remember, in version version 2.0 of the ftrack-python-api the default
    # behavior will change from True to False.
    session = ftrack_api.Session(auto_connect_event_hub=True)
    register(session)
    logging.info(
        'Registered location {} and listening'
        ' for events. Use Ctrl-C to abort.'.format({{cookiecutter.location_name}}Structure.name)
    )
    session.event_hub.wait()
