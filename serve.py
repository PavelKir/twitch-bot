#!/usr/bin/env python
from sys import argv
import win32gui

from src.bot import *
from src.config.config import *
bot = Roboraj(config).run()
