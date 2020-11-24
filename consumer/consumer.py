#!/usr/bin/env python3

# dbus includes
import dbus

ECHO_BUS_NAME = 'com.hello.world'
ECHO_OBJECT_PATH = '/com/hello/world'
ECHO_INTERFACE = 'com.hello.interface'


def client(mes):
    bus = dbus.SessionBus()

    try:
        proxy = bus.get_object(ECHO_BUS_NAME, ECHO_OBJECT_PATH)
    except dbus.DBusException as e:
        # There are actually two exceptions thrown:
        # 1: org.freedesktop.DBus.Error.NameHasNoOwner
        #   (when the name is not registered by any running process)
        # 2: org.freedesktop.DBus.Error.ServiceUnknown
        #   (during auto-activation since there is no .service file)
        # TODO figure out how to suppress the activation attempt
        # also, there *has* to be a better way of managing exceptions
        if e._dbus_error_name != 'org.freedesktop.DBus.Error.ServiceUnknown':
            raise
        if e.__context__._dbus_error_name != 'org.freedesktop.DBus.Error.NameHasNoOwner':
            raise
        print(e)
        print('client: No one can hear me!!')
    else:
        iface = dbus.Interface(proxy, ECHO_INTERFACE)
        iface.echo(mes)


if __name__ == '__main__':
    client('Hello from the consumer')
