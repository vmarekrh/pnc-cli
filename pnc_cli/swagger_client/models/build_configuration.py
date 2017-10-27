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

from datetime import datetime
from pprint import pformat
from six import iteritems


class BuildConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'build_script': 'str',
            'repository_configuration': 'RepositoryConfiguration',
            'scm_revision': 'str',
            'description': 'str',
            'product_version': 'ProductVersion',
            'project': 'Project',
            'build_environment': 'BuildEnvironment',
            'build_configuration_sets': 'list[BuildConfigurationSet]',
            'creation_time': 'datetime',
            'last_modification_time': 'datetime',
            'dependencies': 'list[BuildConfiguration]',
            'dependants': 'list[BuildConfiguration]',
            'generic_parameters': 'dict(str, str)',
            'all_dependencies': 'list[BuildConfiguration]',
            'indirect_dependencies': 'list[BuildConfiguration]',
            'archived': 'bool',
            'field_handler': 'FieldHandler',
            'current_product_milestone': 'ProductMilestone'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'build_script': 'buildScript',
            'repository_configuration': 'repositoryConfiguration',
            'scm_revision': 'scmRevision',
            'description': 'description',
            'product_version': 'productVersion',
            'project': 'project',
            'build_environment': 'buildEnvironment',
            'build_configuration_sets': 'buildConfigurationSets',
            'creation_time': 'creationTime',
            'last_modification_time': 'lastModificationTime',
            'dependencies': 'dependencies',
            'dependants': 'dependants',
            'generic_parameters': 'genericParameters',
            'all_dependencies': 'allDependencies',
            'indirect_dependencies': 'indirectDependencies',
            'archived': 'archived',
            'field_handler': 'fieldHandler',
            'current_product_milestone': 'currentProductMilestone'
        }

        self._id = None
        self._name = None
        self._build_script = None
        self._repository_configuration = None
        self._scm_revision = None
        self._description = None
        self._product_version = None
        self._project = None
        self._build_environment = None
        self._build_configuration_sets = None
        self._creation_time = None
        self._last_modification_time = None
        self._dependencies = None
        self._dependants = None
        self._generic_parameters = None
        self._all_dependencies = None
        self._indirect_dependencies = None
        self._archived = None
        self._field_handler = None
        self._current_product_milestone = None

    @property
    def id(self):
        """
        Gets the id of this BuildConfiguration.


        :return: The id of this BuildConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildConfiguration.


        :param id: The id of this BuildConfiguration.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this BuildConfiguration.


        :return: The name of this BuildConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BuildConfiguration.


        :param name: The name of this BuildConfiguration.
        :type: str
        """
        self._name = name

    @property
    def build_script(self):
        """
        Gets the build_script of this BuildConfiguration.


        :return: The build_script of this BuildConfiguration.
        :rtype: str
        """
        return self._build_script

    @build_script.setter
    def build_script(self, build_script):
        """
        Sets the build_script of this BuildConfiguration.


        :param build_script: The build_script of this BuildConfiguration.
        :type: str
        """
        self._build_script = build_script

    @property
    def repository_configuration(self):
        """
        Gets the repository_configuration of this BuildConfiguration.


        :return: The repository_configuration of this BuildConfiguration.
        :rtype: RepositoryConfiguration
        """
        return self._repository_configuration

    @repository_configuration.setter
    def repository_configuration(self, repository_configuration):
        """
        Sets the repository_configuration of this BuildConfiguration.


        :param repository_configuration: The repository_configuration of this BuildConfiguration.
        :type: RepositoryConfiguration
        """
        self._repository_configuration = repository_configuration

    @property
    def scm_revision(self):
        """
        Gets the scm_revision of this BuildConfiguration.


        :return: The scm_revision of this BuildConfiguration.
        :rtype: str
        """
        return self._scm_revision

    @scm_revision.setter
    def scm_revision(self, scm_revision):
        """
        Sets the scm_revision of this BuildConfiguration.


        :param scm_revision: The scm_revision of this BuildConfiguration.
        :type: str
        """
        self._scm_revision = scm_revision

    @property
    def description(self):
        """
        Gets the description of this BuildConfiguration.


        :return: The description of this BuildConfiguration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BuildConfiguration.


        :param description: The description of this BuildConfiguration.
        :type: str
        """
        self._description = description

    @property
    def product_version(self):
        """
        Gets the product_version of this BuildConfiguration.


        :return: The product_version of this BuildConfiguration.
        :rtype: ProductVersion
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this BuildConfiguration.


        :param product_version: The product_version of this BuildConfiguration.
        :type: ProductVersion
        """
        self._product_version = product_version

    @property
    def project(self):
        """
        Gets the project of this BuildConfiguration.


        :return: The project of this BuildConfiguration.
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this BuildConfiguration.


        :param project: The project of this BuildConfiguration.
        :type: Project
        """
        self._project = project

    @property
    def build_environment(self):
        """
        Gets the build_environment of this BuildConfiguration.


        :return: The build_environment of this BuildConfiguration.
        :rtype: BuildEnvironment
        """
        return self._build_environment

    @build_environment.setter
    def build_environment(self, build_environment):
        """
        Sets the build_environment of this BuildConfiguration.


        :param build_environment: The build_environment of this BuildConfiguration.
        :type: BuildEnvironment
        """
        self._build_environment = build_environment

    @property
    def build_configuration_sets(self):
        """
        Gets the build_configuration_sets of this BuildConfiguration.


        :return: The build_configuration_sets of this BuildConfiguration.
        :rtype: list[BuildConfigurationSet]
        """
        return self._build_configuration_sets

    @build_configuration_sets.setter
    def build_configuration_sets(self, build_configuration_sets):
        """
        Sets the build_configuration_sets of this BuildConfiguration.


        :param build_configuration_sets: The build_configuration_sets of this BuildConfiguration.
        :type: list[BuildConfigurationSet]
        """
        self._build_configuration_sets = build_configuration_sets

    @property
    def creation_time(self):
        """
        Gets the creation_time of this BuildConfiguration.


        :return: The creation_time of this BuildConfiguration.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this BuildConfiguration.


        :param creation_time: The creation_time of this BuildConfiguration.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def last_modification_time(self):
        """
        Gets the last_modification_time of this BuildConfiguration.


        :return: The last_modification_time of this BuildConfiguration.
        :rtype: datetime
        """
        return self._last_modification_time

    @last_modification_time.setter
    def last_modification_time(self, last_modification_time):
        """
        Sets the last_modification_time of this BuildConfiguration.


        :param last_modification_time: The last_modification_time of this BuildConfiguration.
        :type: datetime
        """
        self._last_modification_time = last_modification_time

    @property
    def dependencies(self):
        """
        Gets the dependencies of this BuildConfiguration.


        :return: The dependencies of this BuildConfiguration.
        :rtype: list[BuildConfiguration]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this BuildConfiguration.


        :param dependencies: The dependencies of this BuildConfiguration.
        :type: list[BuildConfiguration]
        """
        self._dependencies = dependencies

    @property
    def dependants(self):
        """
        Gets the dependants of this BuildConfiguration.


        :return: The dependants of this BuildConfiguration.
        :rtype: list[BuildConfiguration]
        """
        return self._dependants

    @dependants.setter
    def dependants(self, dependants):
        """
        Sets the dependants of this BuildConfiguration.


        :param dependants: The dependants of this BuildConfiguration.
        :type: list[BuildConfiguration]
        """
        self._dependants = dependants

    @property
    def generic_parameters(self):
        """
        Gets the generic_parameters of this BuildConfiguration.


        :return: The generic_parameters of this BuildConfiguration.
        :rtype: dict(str, str)
        """
        return self._generic_parameters

    @generic_parameters.setter
    def generic_parameters(self, generic_parameters):
        """
        Sets the generic_parameters of this BuildConfiguration.


        :param generic_parameters: The generic_parameters of this BuildConfiguration.
        :type: dict(str, str)
        """
        self._generic_parameters = generic_parameters

    @property
    def all_dependencies(self):
        """
        Gets the all_dependencies of this BuildConfiguration.


        :return: The all_dependencies of this BuildConfiguration.
        :rtype: list[BuildConfiguration]
        """
        return self._all_dependencies

    @all_dependencies.setter
    def all_dependencies(self, all_dependencies):
        """
        Sets the all_dependencies of this BuildConfiguration.


        :param all_dependencies: The all_dependencies of this BuildConfiguration.
        :type: list[BuildConfiguration]
        """
        self._all_dependencies = all_dependencies

    @property
    def indirect_dependencies(self):
        """
        Gets the indirect_dependencies of this BuildConfiguration.


        :return: The indirect_dependencies of this BuildConfiguration.
        :rtype: list[BuildConfiguration]
        """
        return self._indirect_dependencies

    @indirect_dependencies.setter
    def indirect_dependencies(self, indirect_dependencies):
        """
        Sets the indirect_dependencies of this BuildConfiguration.


        :param indirect_dependencies: The indirect_dependencies of this BuildConfiguration.
        :type: list[BuildConfiguration]
        """
        self._indirect_dependencies = indirect_dependencies

    @property
    def archived(self):
        """
        Gets the archived of this BuildConfiguration.


        :return: The archived of this BuildConfiguration.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """
        Sets the archived of this BuildConfiguration.


        :param archived: The archived of this BuildConfiguration.
        :type: bool
        """
        self._archived = archived

    @property
    def field_handler(self):
        """
        Gets the field_handler of this BuildConfiguration.


        :return: The field_handler of this BuildConfiguration.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this BuildConfiguration.


        :param field_handler: The field_handler of this BuildConfiguration.
        :type: FieldHandler
        """
        self._field_handler = field_handler

    @property
    def current_product_milestone(self):
        """
        Gets the current_product_milestone of this BuildConfiguration.


        :return: The current_product_milestone of this BuildConfiguration.
        :rtype: ProductMilestone
        """
        return self._current_product_milestone

    @current_product_milestone.setter
    def current_product_milestone(self, current_product_milestone):
        """
        Sets the current_product_milestone of this BuildConfiguration.


        :param current_product_milestone: The current_product_milestone of this BuildConfiguration.
        :type: ProductMilestone
        """
        self._current_product_milestone = current_product_milestone

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
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
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
