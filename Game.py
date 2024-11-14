import configparser
import inspect
import random
import re
import sys
from time import sleep

from core import ClientCore

from enums import (
    CharacterSex,
    ActionType,
    TileTypes,
    EquipmentSlots,
    ItemTypes,
)