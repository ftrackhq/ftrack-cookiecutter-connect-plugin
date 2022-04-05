# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

import ftrack_api.accessor.disk


class {{cookiecutter.location_name}}Accessor(ftrack_api.accessor.disk.DiskAccessor):

    def __init__(self, prefix,**kw):
        super({{cookiecutter.location_name}}Accessor, self).__init__(prefix,**kw)