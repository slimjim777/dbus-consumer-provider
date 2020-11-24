#!/usr/bin/env python3

# standard includes
import sys

# dbus includes
import gi.repository.GLib
import dbus
import dbus.service
import dbus.mainloop.glib

ECHO_BUS_NAME = 'com.hello.world'
ECHO_OBJECT_PATH = '/com/hello/world'
ECHO_INTERFACE = 'com.hello.interface'


class EchoServerObject(dbus.service.Object):

    # TODO it would be nice to make a better decorator using annotations:
    #   def foo(self, a: 's', b: 's') -> '': pass
    # but the existing dbus decorator does its own reflection which
    # fails if there are any annotations (or keyword-only arguments)
    @dbus.service.method(ECHO_INTERFACE,
                         in_signature='s', out_signature='')
    def echo(self, message):
        message = str(message)  # get rid of subclass for repr
        print('server: a client said %r' % message)


def server():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    bus = dbus.SessionBus()
    try:
        name = dbus.service.BusName(ECHO_BUS_NAME, bus, do_not_queue=True)
    except dbus.NameExistsException:
        sys.exit('Server is already running.')
    else:
        print('Server is not running yet. Putting on listening ears.')
    echo = EchoServerObject(bus, ECHO_OBJECT_PATH)

    mainloop = gi.repository.GLib.MainLoop()
    echo.mainloop = mainloop
    mainloop.run()


if __name__ == '__main__':
    server()
