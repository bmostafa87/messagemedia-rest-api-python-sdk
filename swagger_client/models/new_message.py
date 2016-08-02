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

from pprint import pformat
from six import iteritems
import re


class NewMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, content=None, callback_url=None, delivery_report=False, destination_number=None, format='SMS', metadata=None, message_expiry_timestamp=None, scheduled=None, source_address=None, source_address_type=None):
        """
        NewMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'str',
            'callback_url': 'str',
            'delivery_report': 'bool',
            'destination_number': 'str',
            'format': 'str',
            'metadata': 'MessageMetadata',
            'message_expiry_timestamp': 'datetime',
            'scheduled': 'datetime',
            'source_address': 'str',
            'source_address_type': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'callback_url': 'callback_url',
            'delivery_report': 'delivery_report',
            'destination_number': 'destination_number',
            'format': 'format',
            'metadata': 'metadata',
            'message_expiry_timestamp': 'message_expiry_timestamp',
            'scheduled': 'scheduled',
            'source_address': 'source_address',
            'source_address_type': 'source_address_type'
        }

        self._content = content
        self._callback_url = callback_url
        self._delivery_report = delivery_report
        self._destination_number = destination_number
        self._format = format
        self._metadata = metadata
        self._message_expiry_timestamp = message_expiry_timestamp
        self._scheduled = scheduled
        self._source_address = source_address
        self._source_address_type = source_address_type

    @property
    def content(self):
        """
        Gets the content of this NewMessage.
        Content of message.

        :return: The content of this NewMessage.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this NewMessage.
        Content of message.

        :param content: The content of this NewMessage.
        :type: str
        """

        if not content:
            raise ValueError("Invalid value for `content`, must not be `None`")
        if len(content) > 5000:
            raise ValueError("Invalid value for `content`, length must be less than `5000`")
        if len(content) < 1:
            raise ValueError("Invalid value for `content`, length must be greater than or equal to `1`")

        self._content = content

    @property
    def callback_url(self):
        """
        Gets the callback_url of this NewMessage.
        URL replies and delivery reports to this message will be pushed to.

        :return: The callback_url of this NewMessage.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this NewMessage.
        URL replies and delivery reports to this message will be pushed to.

        :param callback_url: The callback_url of this NewMessage.
        :type: str
        """

        self._callback_url = callback_url

    @property
    def delivery_report(self):
        """
        Gets the delivery_report of this NewMessage.


        :return: The delivery_report of this NewMessage.
        :rtype: bool
        """
        return self._delivery_report

    @delivery_report.setter
    def delivery_report(self, delivery_report):
        """
        Sets the delivery_report of this NewMessage.


        :param delivery_report: The delivery_report of this NewMessage.
        :type: bool
        """

        self._delivery_report = delivery_report

    @property
    def destination_number(self):
        """
        Gets the destination_number of this NewMessage.
        Destination number of the message.

        :return: The destination_number of this NewMessage.
        :rtype: str
        """
        return self._destination_number

    @destination_number.setter
    def destination_number(self, destination_number):
        """
        Sets the destination_number of this NewMessage.
        Destination number of the message.

        :param destination_number: The destination_number of this NewMessage.
        :type: str
        """

        if not destination_number:
            raise ValueError("Invalid value for `destination_number`, must not be `None`")
        if len(destination_number) > 15:
            raise ValueError("Invalid value for `destination_number`, length must be less than `15`")
        if len(destination_number) < 1:
            raise ValueError("Invalid value for `destination_number`, length must be greater than or equal to `1`")

        self._destination_number = destination_number

    @property
    def format(self):
        """
        Gets the format of this NewMessage.
        Format of message.

        :return: The format of this NewMessage.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this NewMessage.
        Format of message.

        :param format: The format of this NewMessage.
        :type: str
        """
        allowed_values = ["SMS", "VOICE"]
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def metadata(self):
        """
        Gets the metadata of this NewMessage.


        :return: The metadata of this NewMessage.
        :rtype: MessageMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this NewMessage.


        :param metadata: The metadata of this NewMessage.
        :type: MessageMetadata
        """

        self._metadata = metadata

    @property
    def message_expiry_timestamp(self):
        """
        Gets the message_expiry_timestamp of this NewMessage.
        Date time after which the message is considered expired in ISO8601 format.

        :return: The message_expiry_timestamp of this NewMessage.
        :rtype: datetime
        """
        return self._message_expiry_timestamp

    @message_expiry_timestamp.setter
    def message_expiry_timestamp(self, message_expiry_timestamp):
        """
        Sets the message_expiry_timestamp of this NewMessage.
        Date time after which the message is considered expired in ISO8601 format.

        :param message_expiry_timestamp: The message_expiry_timestamp of this NewMessage.
        :type: datetime
        """

        self._message_expiry_timestamp = message_expiry_timestamp

    @property
    def scheduled(self):
        """
        Gets the scheduled of this NewMessage.
        Date time at which the message is scheduled for in ISO8601 format.

        :return: The scheduled of this NewMessage.
        :rtype: datetime
        """
        return self._scheduled

    @scheduled.setter
    def scheduled(self, scheduled):
        """
        Sets the scheduled of this NewMessage.
        Date time at which the message is scheduled for in ISO8601 format.

        :param scheduled: The scheduled of this NewMessage.
        :type: datetime
        """

        self._scheduled = scheduled

    @property
    def source_address(self):
        """
        Gets the source_address of this NewMessage.


        :return: The source_address of this NewMessage.
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """
        Sets the source_address of this NewMessage.


        :param source_address: The source_address of this NewMessage.
        :type: str
        """

        if not source_address:
            raise ValueError("Invalid value for `source_address`, must not be `None`")
        if len(source_address) > 14:
            raise ValueError("Invalid value for `source_address`, length must be less than `14`")
        if len(source_address) < 1:
            raise ValueError("Invalid value for `source_address`, length must be greater than or equal to `1`")

        self._source_address = source_address

    @property
    def source_address_type(self):
        """
        Gets the source_address_type of this NewMessage.
        Type of source address specified.

        :return: The source_address_type of this NewMessage.
        :rtype: str
        """
        return self._source_address_type

    @source_address_type.setter
    def source_address_type(self, source_address_type):
        """
        Sets the source_address_type of this NewMessage.
        Type of source address specified.

        :param source_address_type: The source_address_type of this NewMessage.
        :type: str
        """
        allowed_values = ["INTERNATIONAL", "ALPHANUMERIC", "SHORTCODE"]
        if source_address_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_address_type` ({0}), must be one of {1}"
                .format(source_address_type, allowed_values)
            )

        self._source_address_type = source_address_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
