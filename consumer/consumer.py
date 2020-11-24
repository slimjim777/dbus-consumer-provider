#!/usr/bin/env python3

# dbus includes
import dbus

ECHO_BUS_NAME = 'com.hello.world.Demo'
ECHO_OBJECT_PATH = '/com/hello/world/Demo'
ECHO_INTERFACE = 'com.hello.world.Demo'


def client(mes):
    bus = dbus.SystemBus()

    try:
        proxy = bus.get_object(ECHO_BUS_NAME, ECHO_OBJECT_PATH)
    except dbus.DBusException as e:
        if e._dbus_error_name != 'org.freedesktop.DBus.Error.ServiceUnknown':
            raise
        if e.__context__._dbus_error_name != 'org.freedesktop.DBus.Error.NameHasNoOwner':
            raise
        print(e)
        print('client: No one can hear me!!')
    else:
        iface = dbus.Interface(proxy, ECHO_INTERFACE)
        iface.Foo(mes)


if __name__ == '__main__':
    client('Hello from the consumer')
