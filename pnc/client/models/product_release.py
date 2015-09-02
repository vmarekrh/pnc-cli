# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ProductRelease(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProductRelease - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'version': 'str',
            'release_date': 'datetime',
            'download_url': 'str',
            'product_version_id': 'int',
            'product_milestone_id': 'int',
            'support_level': 'SupportLevel'
        }

        self.attribute_map = {
            'id': 'id',
            'version': 'version',
            'release_date': 'releaseDate',
            'download_url': 'downloadUrl',
            'product_version_id': 'productVersionId',
            'product_milestone_id': 'productMilestoneId',
            'support_level': 'supportLevel'
        }

        self._id = None
        self._version = None
        self._release_date = None
        self._download_url = None
        self._product_version_id = None
        self._product_milestone_id = None
        self._support_level = None

    @property
    def id(self):
        """
        Gets the id of this ProductRelease.


        :return: The id of this ProductRelease.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductRelease.


        :param id: The id of this ProductRelease.
        :type: int
        """
        self._id = id

    @property
    def version(self):
        """
        Gets the version of this ProductRelease.


        :return: The version of this ProductRelease.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ProductRelease.


        :param version: The version of this ProductRelease.
        :type: str
        """
        self._version = version

    @property
    def release_date(self):
        """
        Gets the release_date of this ProductRelease.


        :return: The release_date of this ProductRelease.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this ProductRelease.


        :param release_date: The release_date of this ProductRelease.
        :type: datetime
        """
        self._release_date = release_date

    @property
    def download_url(self):
        """
        Gets the download_url of this ProductRelease.


        :return: The download_url of this ProductRelease.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """
        Sets the download_url of this ProductRelease.


        :param download_url: The download_url of this ProductRelease.
        :type: str
        """
        self._download_url = download_url

    @property
    def product_version_id(self):
        """
        Gets the product_version_id of this ProductRelease.


        :return: The product_version_id of this ProductRelease.
        :rtype: int
        """
        return self._product_version_id

    @product_version_id.setter
    def product_version_id(self, product_version_id):
        """
        Sets the product_version_id of this ProductRelease.


        :param product_version_id: The product_version_id of this ProductRelease.
        :type: int
        """
        self._product_version_id = product_version_id

    @property
    def product_milestone_id(self):
        """
        Gets the product_milestone_id of this ProductRelease.


        :return: The product_milestone_id of this ProductRelease.
        :rtype: int
        """
        return self._product_milestone_id

    @product_milestone_id.setter
    def product_milestone_id(self, product_milestone_id):
        """
        Sets the product_milestone_id of this ProductRelease.


        :param product_milestone_id: The product_milestone_id of this ProductRelease.
        :type: int
        """
        self._product_milestone_id = product_milestone_id

    @property
    def support_level(self):
        """
        Gets the support_level of this ProductRelease.


        :return: The support_level of this ProductRelease.
        :rtype: SupportLevel
        """
        return self._support_level

    @support_level.setter
    def support_level(self, support_level):
        """
        Sets the support_level of this ProductRelease.


        :param support_level: The support_level of this ProductRelease.
        :type: SupportLevel
        """
        self._support_level = support_level

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
