# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

import ftrack_api.structure.standard


class {{cookiecutter.location_name}}Structure(ftrack_api.structure.standard.StandardStructure):

    description = 'Templated example structure from ftrack-recipes'
    name = 'structure.{{cookiecutter.location_name}}'

    def __init__(
        self, project_versions_prefix=None, illegal_character_substitute='_'
    ):
        super({{cookiecutter.location_name}}Structure, self).__init__(
            project_versions_prefix= project_versions_prefix,
            illegal_character_substitute=illegal_character_substitute
        )
