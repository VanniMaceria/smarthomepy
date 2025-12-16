import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_room_is_occupied(self, infrared: Mock):
        smartroom = SmartRoom()
        infrared.return_value = True
        outcome = smartroom.check_room_occupancy()
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_check_room_is_not_occupied(self, infrared: Mock):
        smartroom = SmartRoom()
        infrared.return_value = False
        outcome = smartroom.check_room_occupancy()
        self.assertFalse(outcome)

    @patch.object(GPIO, "input")
    def test_there_is_enough_light(self, photoresistor: Mock):
        smartroom = SmartRoom()
        photoresistor.return_value = True
        outcome = smartroom.check_enough_light()
        self.assertTrue(outcome)

    @patch.object(GPIO, "input")
    def test_there_is_not_enough_light(self, photoresistor: Mock):
        smartroom = SmartRoom()
        photoresistor.return_value = False
        outcome = smartroom.check_enough_light()
        self.assertFalse(outcome)