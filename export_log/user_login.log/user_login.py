# -*- encoding=utf8 -*-
__author__ = "caijp"

from airtest.core.api import *

auto_setup(__file__)
package = "com.netease.pq"
start_app(package)
back = wait(Template(r"tpl1621138104988.png", record_pos=(0.463, 0.234), resolution=(1920, 1080)), timeout = 60, interval = 10)
touch(back)