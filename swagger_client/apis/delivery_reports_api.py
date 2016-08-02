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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DeliveryReportsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delivery_reports_confirmed_post(self, delivery_report_id, **kwargs):
        """
        Confirm the receipt of delivery reports.
        The confirm delivery reports endpoint will update the specified delivery reports as confirmed, confirmed delivery reports will no longer be returned in check delivery reports requests.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delivery_reports_confirmed_post(delivery_report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeliveryReportId delivery_report_id: A list of delivery report IDs to mark as confirmed. (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delivery_reports_confirmed_post_with_http_info(delivery_report_id, **kwargs)
        else:
            (data) = self.delivery_reports_confirmed_post_with_http_info(delivery_report_id, **kwargs)
            return data

    def delivery_reports_confirmed_post_with_http_info(self, delivery_report_id, **kwargs):
        """
        Confirm the receipt of delivery reports.
        The confirm delivery reports endpoint will update the specified delivery reports as confirmed, confirmed delivery reports will no longer be returned in check delivery reports requests.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delivery_reports_confirmed_post_with_http_info(delivery_report_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeliveryReportId delivery_report_id: A list of delivery report IDs to mark as confirmed. (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_report_id', 'account']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delivery_reports_confirmed_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_report_id' is set
        if ('delivery_report_id' not in params) or (params['delivery_report_id'] is None):
            raise ValueError("Missing the required parameter `delivery_report_id` when calling `delivery_reports_confirmed_post`")

        resource_path = '/delivery_reports/confirmed'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'account' in params:
            header_params['Account'] = params['account']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delivery_report_id' in params:
            body_params = params['delivery_report_id']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['hmac']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def delivery_reports_get(self, **kwargs):
        """
        This endpoint is used to check for unconfirmed reports.
        The reports endpoint returns the first 100 delivery reports that have been received and haven't been confirmed using the confirm reports endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delivery_reports_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: DeliveryReports
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delivery_reports_get_with_http_info(**kwargs)
        else:
            (data) = self.delivery_reports_get_with_http_info(**kwargs)
            return data

    def delivery_reports_get_with_http_info(self, **kwargs):
        """
        This endpoint is used to check for unconfirmed reports.
        The reports endpoint returns the first 100 delivery reports that have been received and haven't been confirmed using the confirm reports endpoint.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delivery_reports_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: DeliveryReports
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delivery_reports_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/delivery_reports'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'account' in params:
            header_params['Account'] = params['account']

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['hmac']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='DeliveryReports',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
