#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# CChatServer daemon
# 
# Server for CChat.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# ----------------------------------------------------------------

from daemon3x import Daemon
from server import cchat_run

import sys

pid = "/tmp/cchat.pid"
wd = "/data/CChatServer/"

class MyDaemon(Daemon):
    def run(self):
        cchat_run()

if __name__ == "__main__":
    daemon = MyDaemon(pid, wd)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart" % sys.argv[0])
        sys.exit(2)