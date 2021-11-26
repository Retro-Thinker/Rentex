# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse20013(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, location_id: int = None):  # noqa: E501
        """InlineResponse20013 - a model defined in Swagger

        :param location_id: The location_id of this InlineResponse20013.  # noqa: E501
        :type location_id: int
        """
        self.swagger_types = {
            'location_id': int
        }

        self.attribute_map = {
            'location_id': 'locationId'
        }
        self._location_id = location_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20013':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_13 of this InlineResponse20013.  # noqa: E501
        :rtype: InlineResponse20013
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location_id(self) -> int:
        """Gets the location_id of this InlineResponse20013.

        Id nowej lokacji  # noqa: E501

        :return: The location_id of this InlineResponse20013.
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id: int):
        """Sets the location_id of this InlineResponse20013.

        Id nowej lokacji  # noqa: E501

        :param location_id: The location_id of this InlineResponse20013.
        :type location_id: int
        """

        self._location_id = location_id