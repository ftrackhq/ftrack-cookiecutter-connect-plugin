# :coding: utf-8
# :copyright: Copyright (c) 2014-2020 ftrack

import ftrack_api.resource_identifier_transformer.base


class {{cookiecutter.location_name}}Transformer(ftrack_api.resource_identifier_transformer.base.ResourceIdentifierTransformer):

    def __init__(self, session):
        super({{cookiecutter.location_name}}Transformer, self).__init__(session)