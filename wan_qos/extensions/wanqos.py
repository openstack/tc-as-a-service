# Copyright 2016 Huawei corp.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

from neutron_lib.api import extensions
from neutron.api.v2 import resource_helper

from wan_qos.common import constants

RESOURCE_ATTRIBUTE_MAP = {
    constants.WAN_QOS: {
        'id': {'allow_post': False, 'allow_put': False,
               'is_visible': True},
        'max_rate': {'allow_post': True, 'allow_put': False,
                          'validate': {'type:string': None},
                          'is_visible': True, 'default': ''},
        'min_rate': {'allow_post': True, 'allow_put': False,
                     'validate': {'type:string': None},
                     'is_visible': True, 'default': ''},
        'network_id': {'allow_post': True, 'allow_put': False,
                       'validate': {'type:string': None},
                       'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'validate': {'type:string': None},
                      'required_by_policy': True,
                      'is_visible': True}
    },
}


class WanQos(extensions.ExtensionDescriptor):

    @classmethod
    def get_name(cls):
        return "WAN QoS"

    @classmethod
    def get_alias(cls):
        return "wan_qos"

    @classmethod
    def get_description(cls):
        return "Limit traffic on WAN links"

    @classmethod
    def get_updated(cls):
        return "2016-12-01T00:00:00-00:00"

    @classmethod
    def get_resources(cls):
        """Returns Ext Resources."""

        mem_actions = {}
        plural_mappings = resource_helper.build_plural_mappings(
            {}, RESOURCE_ATTRIBUTE_MAP)
        resources = resource_helper.build_resource_info(plural_mappings,
                                                        RESOURCE_ATTRIBUTE_MAP,
                                                        constants.WANQOS,
                                                        action_map=mem_actions,
                                                        register_quota=True,
                                                        translate_name=True)

        return resources

    def get_extended_resources(self, version):
        if version == "2.0":
            return RESOURCE_ATTRIBUTE_MAP
        else:
            return {}


class WanQosPluginBase(object):

    @abc.abstractmethod
    def create_wan_qos(self, context, wan_qos):
        pass

    @abc.abstractmethod
    def get_wan_qos(self, id):
        pass

    @abc.abstractmethod
    def get_wan_qoss(self):
        pass

    @abc.abstractmethod
    def update_wan_qos(self, context, id, wan_qos):
        pass

    @abc.abstractmethod
    def delete_wan_qos(self, context, id):
        pass
