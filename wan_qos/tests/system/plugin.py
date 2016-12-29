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


import time
import sys

from oslo_config import cfg
from oslo_service import service

from neutron.agent.common import config
from neutron.common import config as common_config
from neutron import service as neutron_service

from wan_qos.common import topics
from wan_qos.services import plugin


def main():
    common_config.init(sys.argv[1:])
    config.setup_logging()
    wanqos_plugin = plugin.WanQosPlugin()
    while True:
        time.sleep(3)

if __name__ == '__main__':
    main()
