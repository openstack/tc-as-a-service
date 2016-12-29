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

import oslo_messaging

from neutron.common import rpc as n_rpc

from wan_qos.common import topics


class TcPluginApi(object):
    def __init__(self, host, topic=topics.TC_PLUGIN):
        self.host = host
        target = oslo_messaging.Target(topic=topic, version='1.0')
        self.client = n_rpc.get_client(target)

    def agent_up_notification(self, context):
        cctxt = self.client.prepare()
        return cctxt.cast(context, 'agent_up_notification', host=self.host)

    def get_configuration_from_db(self, context):
        cctxt = self.client.prepare()
        return cctxt.call(context, 'get_configuration_from_db', host=self.host)


class TcAgentApi(object):
    def __init__(self, host, topic=topics.TC_AGENT):
        self.host = host
        target = oslo_messaging.Target(topic=topic, version='1.0')
        self.client = n_rpc.get_client(target)

    def create_wan_qos(self, context, wan_qos_dict):
        cctxt = self.client.prepare()
        return cctxt.call(context,
                          'create_wan_qos',
                          wan_qos_dict)

