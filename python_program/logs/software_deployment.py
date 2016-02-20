#soumiyajit
	from oslo_log import log as logging
	from heat.common.i18n import _LE
	from heat.common.i18n import _LI
	LOG = logging.getLogger(__name__)#soumiyajit
from oslo_log import log as logging
from heat.common.i18n import _LE
from heat.common.i18n import _LI
LOG = logging.getLogger(__name__)# Copyright 2014 Intel Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
SoftwareDeployment object
"""


from oslo_versionedobjects import base
from oslo_versionedobjects import fields

from heat.db import api as db_api
from heat.objects import fields as heat_fields
from heat.objects import software_config


class SoftwareDeployment(base.VersionedObject,
    LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeployment "))
                         base.VersionedObjectDictCompat,
                         base.ComparableVersionedObject):
    fields = {
        'id': fields.StringField(nullable=False),
        'config_id': fields.StringField(nullable=False),
        'server_id': fields.StringField(nullable=False),
        'input_values': heat_fields.JsonField(nullable=True),
        'output_values': heat_fields.JsonField(nullable=True),
        'tenant': fields.StringField(nullable=False),
        'stack_user_project_id': fields.StringField(nullable=True),
        'action': fields.StringField(nullable=True),
        'status': fields.StringField(nullable=True),
        'status_reason': fields.StringField(nullable=True),
        'config': fields.ObjectField('SoftwareConfig'),
        'created_at': fields.DateTimeField(read_only=True),
        'updated_at': fields.DateTimeField(nullable=True),
    }

    @staticmethod
    def _from_db_object(context, deployment, db_deployment):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeployment_from_db_object "))
        : LOG.info(_LI("soumiyajit::  class SoftwareDeployment(base.VersionedObject, "))
        for field in deployment.fields:
            if field == 'config':
                deployment[field] = (
                    software_config.SoftwareConfig._from_db_object(
                        context, software_config.SoftwareConfig(),
                        db_deployment['config'])
                )
            else:
                deployment[field] = db_deployment[field]
        deployment._context = context
        deployment.obj_reset_changes()
        return deployment

    @classmethod
    def create(cls, context, values):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeploymentcreate "))
        : LOG.info(_LI("soumiyajit::  class SoftwareDeployment(base.VersionedObject, "))
        return cls._from_db_object(
            context, cls(), db_api.software_deployment_create(context, values))

    @classmethod
    def get_by_id(cls, context, deployment_id):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeploymentget_by_id "))
        : LOG.info(_LI("soumiyajit::  class SoftwareDeployment(base.VersionedObject, "))
        return cls._from_db_object(
            context, cls(),
            db_api.software_deployment_get(context, deployment_id))

    @classmethod
    def get_all(cls, context, server_id=None):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeploymentget_all "))
        : LOG.info(_LI("soumiyajit::  class SoftwareDeployment(base.VersionedObject, "))
        return [cls._from_db_object(context, cls(), db_deployment)
                for db_deployment in db_api.software_deployment_get_all(
                    context, server_id)]

    @classmethod
    def update_by_id(cls, context, deployment_id, values):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeploymentupdate_by_id "))
        : LOG.info(_LI("soumiyajit::  class SoftwareDeployment(base.VersionedObject, "))
        return cls._from_db_object(
            context, cls(),
            db_api.software_deployment_update(context, deployment_id, values))

    @classmethod
    def delete(cls, context, deployment_id):
        LOG.info(_LI("soumiyajit::  /home/pankaj/python_program/logs/software_deployment.py\Class SoftwareDeploymentdelete "))
        : LOG.info(_LI("soumiyajit::  class SoftwareDeployment(base.VersionedObject, "))
        db_api.software_deployment_delete(context, deployment_id)
