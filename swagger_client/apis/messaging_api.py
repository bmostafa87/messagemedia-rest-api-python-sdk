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


class MessagingApi(object):
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

    def messages_message_id_get(self, message_id, **kwargs):
        """
        Retrive the status and details of a submitted message.
        Get the status and details of a previously submitted message

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_message_id_get(message_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_id: Unique identifier representing message that has been submitted (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: Message
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.messages_message_id_get_with_http_info(message_id, **kwargs)
        else:
            (data) = self.messages_message_id_get_with_http_info(message_id, **kwargs)
            return data

    def messages_message_id_get_with_http_info(self, message_id, **kwargs):
        """
        Retrive the status and details of a submitted message.
        Get the status and details of a previously submitted message

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_message_id_get_with_http_info(message_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_id: Unique identifier representing message that has been submitted (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: Message
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id', 'account']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_message_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `messages_message_id_get`")

        resource_path = '/messages/{messageId}'.replace('{format}', 'json')
        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

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
                                            response_type='Message',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def messages_message_id_put(self, message_id, status, **kwargs):
        """
        Update the status of a submitted message.
        Update the status of a scheduled message to cancelled to prevent the message from being sent

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_message_id_put(message_id, status, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_id: Unique identifier representing message to be updated. (required)
        :param Status status: New status for the message. (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.messages_message_id_put_with_http_info(message_id, status, **kwargs)
        else:
            (data) = self.messages_message_id_put_with_http_info(message_id, status, **kwargs)
            return data

    def messages_message_id_put_with_http_info(self, message_id, status, **kwargs):
        """
        Update the status of a submitted message.
        Update the status of a scheduled message to cancelled to prevent the message from being sent

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_message_id_put_with_http_info(message_id, status, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message_id: Unique identifier representing message to be updated. (required)
        :param Status status: New status for the message. (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id', 'status', 'account']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_message_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params) or (params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `messages_message_id_put`")
        # verify the required parameter 'status' is set
        if ('status' not in params) or (params['status'] is None):
            raise ValueError("Missing the required parameter `status` when calling `messages_message_id_put`")

        resource_path = '/messages/{messageId}'.replace('{format}', 'json')
        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']

        query_params = {}

        header_params = {}
        if 'account' in params:
            header_params['Account'] = params['account']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'status' in params:
            body_params = params['status']

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

        return self.api_client.call_api(resource_path, 'PUT',
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

    def messages_post(self, messages, **kwargs):
        """
        Send one or more SMS or text to voice messages.
        Submit one or more (up to 100 per request) SMS or text to voice messages to be sent to the destination address. - A callback URL can be included with each message to which MO and DR notifications will be pushed to via a HTTP POST request. - The content of the message can be a unicode string, up to 5000 characters long - A delivery report can be be requested with the message which will be pushed to a HTTP endpoint if specified, or available via the Check Reports endpoint. - The destination number should be specified in E.164 international format. For information on E.164, please refer to http://en.wikipedia.org/wiki/E.164 - The format specifies which format the message will be sent as, SMS or VOICE - If specified the source number included in the request will be shown as the source number for the message, this feature is not enabled by default, please contact MessageMedia for more information. - If a source number is specified, the type of source number may also be specified. - The message will be scheduled to be delivered in the future if the scheduled parameter is specified. - A message expiry timestamp can be provided, if the message is not delivered by this time, it will be discarded. - Metadata can be included with the message. Up to 5 key value pair strings can be included with each message. This metadata will be available in delivery reports and replies. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_post(messages, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Messages messages: A list of messages to be sent. (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: MessageList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.messages_post_with_http_info(messages, **kwargs)
        else:
            (data) = self.messages_post_with_http_info(messages, **kwargs)
            return data

    def messages_post_with_http_info(self, messages, **kwargs):
        """
        Send one or more SMS or text to voice messages.
        Submit one or more (up to 100 per request) SMS or text to voice messages to be sent to the destination address. - A callback URL can be included with each message to which MO and DR notifications will be pushed to via a HTTP POST request. - The content of the message can be a unicode string, up to 5000 characters long - A delivery report can be be requested with the message which will be pushed to a HTTP endpoint if specified, or available via the Check Reports endpoint. - The destination number should be specified in E.164 international format. For information on E.164, please refer to http://en.wikipedia.org/wiki/E.164 - The format specifies which format the message will be sent as, SMS or VOICE - If specified the source number included in the request will be shown as the source number for the message, this feature is not enabled by default, please contact MessageMedia for more information. - If a source number is specified, the type of source number may also be specified. - The message will be scheduled to be delivered in the future if the scheduled parameter is specified. - A message expiry timestamp can be provided, if the message is not delivered by this time, it will be discarded. - Metadata can be included with the message. Up to 5 key value pair strings can be included with each message. This metadata will be available in delivery reports and replies. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.messages_post_with_http_info(messages, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Messages messages: A list of messages to be sent. (required)
        :param str account: The account to use for this request. This account will be used for the request instead of the account assigned to the API key used to sign the request, allowing one API key to be used to perform requests on behalf of other accounts.
        :return: MessageList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messages', 'account']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method messages_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'messages' is set
        if ('messages' not in params) or (params['messages'] is None):
            raise ValueError("Missing the required parameter `messages` when calling `messages_post`")

        resource_path = '/messages'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'account' in params:
            header_params['Account'] = params['account']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'messages' in params:
            body_params = params['messages']

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
                                            response_type='MessageList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
