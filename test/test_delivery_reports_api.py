# coding: utf-8

"""
    MessageMedia REST API

    Australia’s Leading Messaging Solutions for Business and Enterprise.

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.delivery_reports_api import DeliveryReportsApi


class TestDeliveryReportsApi(unittest.TestCase):
    """ DeliveryReportsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.delivery_reports_api.DeliveryReportsApi()

    def tearDown(self):
        pass

    def test_delivery_reports_confirmed_post(self):
        """
        Test case for delivery_reports_confirmed_post

        Confirm the receipt of delivery reports.
        """
        pass

    def test_delivery_reports_get(self):
        """
        Test case for delivery_reports_get

        This endpoint is used to check for unconfirmed reports.
        """
        pass


if __name__ == '__main__':
    unittest.main()
