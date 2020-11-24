#!/usr/bin/env python3

import gi.repository.GLib
import dbus
import dbus.service
import dbus.mainloop.glib

ECHO_BUS_NAME = 'com.hello.world'
ECHO_OBJECT_PATH = '/com/hello/world'
ECHO_INTERFACE = 'com.hello.interface'


class EchoServerObject(dbus.service.Object):

    def __init__(self):
        bus_name = dbus.service.BusName(ECHO_BUS_NAME, bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, ECHO_OBJECT_PATH)


    @dbus.service.method(ECHO_INTERFACE,
                         in_signature='s', out_signature='')
    def echo(self, message):
        message = str(message)
        print('server: a client said %r' % message)


def server():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    service = EchoServerObject()
    gi.repository.GLib.MainLoop().run()


if __name__ == '__main__':
    server()
