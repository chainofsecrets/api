# coding: utf-8

"""
    API for Secret Network by ChainofSecrets.org

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse2006(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'inflation_rate_change': 'str',
        'inflation_max': 'str',
        'inflation_min': 'str',
        'goal_bonded': 'str',
        'unbonding_time': 'str',
        'max_validators': 'int',
        'bond_denom': 'str'
    }

    attribute_map = {
        'inflation_rate_change': 'inflation_rate_change',
        'inflation_max': 'inflation_max',
        'inflation_min': 'inflation_min',
        'goal_bonded': 'goal_bonded',
        'unbonding_time': 'unbonding_time',
        'max_validators': 'max_validators',
        'bond_denom': 'bond_denom'
    }

    def __init__(self, inflation_rate_change=None, inflation_max=None, inflation_min=None, goal_bonded=None, unbonding_time=None, max_validators=None, bond_denom=None):  # noqa: E501
        """InlineResponse2006 - a model defined in Swagger"""  # noqa: E501

        self._inflation_rate_change = None
        self._inflation_max = None
        self._inflation_min = None
        self._goal_bonded = None
        self._unbonding_time = None
        self._max_validators = None
        self._bond_denom = None
        self.discriminator = None

        if inflation_rate_change is not None:
            self.inflation_rate_change = inflation_rate_change
        if inflation_max is not None:
            self.inflation_max = inflation_max
        if inflation_min is not None:
            self.inflation_min = inflation_min
        if goal_bonded is not None:
            self.goal_bonded = goal_bonded
        if unbonding_time is not None:
            self.unbonding_time = unbonding_time
        if max_validators is not None:
            self.max_validators = max_validators
        if bond_denom is not None:
            self.bond_denom = bond_denom

    @property
    def inflation_rate_change(self):
        """Gets the inflation_rate_change of this InlineResponse2006.  # noqa: E501


        :return: The inflation_rate_change of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._inflation_rate_change

    @inflation_rate_change.setter
    def inflation_rate_change(self, inflation_rate_change):
        """Sets the inflation_rate_change of this InlineResponse2006.


        :param inflation_rate_change: The inflation_rate_change of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._inflation_rate_change = inflation_rate_change

    @property
    def inflation_max(self):
        """Gets the inflation_max of this InlineResponse2006.  # noqa: E501


        :return: The inflation_max of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._inflation_max

    @inflation_max.setter
    def inflation_max(self, inflation_max):
        """Sets the inflation_max of this InlineResponse2006.


        :param inflation_max: The inflation_max of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._inflation_max = inflation_max

    @property
    def inflation_min(self):
        """Gets the inflation_min of this InlineResponse2006.  # noqa: E501


        :return: The inflation_min of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._inflation_min

    @inflation_min.setter
    def inflation_min(self, inflation_min):
        """Sets the inflation_min of this InlineResponse2006.


        :param inflation_min: The inflation_min of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._inflation_min = inflation_min

    @property
    def goal_bonded(self):
        """Gets the goal_bonded of this InlineResponse2006.  # noqa: E501


        :return: The goal_bonded of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._goal_bonded

    @goal_bonded.setter
    def goal_bonded(self, goal_bonded):
        """Sets the goal_bonded of this InlineResponse2006.


        :param goal_bonded: The goal_bonded of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._goal_bonded = goal_bonded

    @property
    def unbonding_time(self):
        """Gets the unbonding_time of this InlineResponse2006.  # noqa: E501


        :return: The unbonding_time of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._unbonding_time

    @unbonding_time.setter
    def unbonding_time(self, unbonding_time):
        """Sets the unbonding_time of this InlineResponse2006.


        :param unbonding_time: The unbonding_time of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._unbonding_time = unbonding_time

    @property
    def max_validators(self):
        """Gets the max_validators of this InlineResponse2006.  # noqa: E501


        :return: The max_validators of this InlineResponse2006.  # noqa: E501
        :rtype: int
        """
        return self._max_validators

    @max_validators.setter
    def max_validators(self, max_validators):
        """Sets the max_validators of this InlineResponse2006.


        :param max_validators: The max_validators of this InlineResponse2006.  # noqa: E501
        :type: int
        """

        self._max_validators = max_validators

    @property
    def bond_denom(self):
        """Gets the bond_denom of this InlineResponse2006.  # noqa: E501


        :return: The bond_denom of this InlineResponse2006.  # noqa: E501
        :rtype: str
        """
        return self._bond_denom

    @bond_denom.setter
    def bond_denom(self, bond_denom):
        """Sets the bond_denom of this InlineResponse2006.


        :param bond_denom: The bond_denom of this InlineResponse2006.  # noqa: E501
        :type: str
        """

        self._bond_denom = bond_denom

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse2006, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2006):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
