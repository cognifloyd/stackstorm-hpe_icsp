# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lib.icsp import ICSPBaseActions


class DeleteServer(ICSPBaseActions):
    def run(self, identifiers, id_type, connection_details=None):
        self.set_connection(connection_details)
        self.get_sessionid()
        if id_type != "mids":
            mids = self.get_mids(identifiers, id_type)
        else:
            mids = identifiers

        for mid in mids:
            try:
                isinstance(mid, int)
            except ValueError:
                raise ValueError("MID values must be numbers")

            endpoint = "/rest/os-deployment-servers/%s" % (mid)
            self.icsp_delete(endpoint)
        return
