package main

import (
	"fmt"
	"os"

	"github.com/godbus/dbus/v5"
	"github.com/godbus/dbus/v5/introspect"
)

const intro = `
<node>
	<interface name="com.hello.world.Demo">
		<method name="Foo">
			<arg direction="in" type="s"/>
		</method>
	</interface>` + introspect.IntrospectDataString + `</node> `

type foo struct {}

func (f foo) Foo(message string) *dbus.Error {
	fmt.Println(f)
	fmt.Println(message)
	return nil
}

func main() {
	conn, err := dbus.SystemBus()
	if err != nil {
		panic(err)
	}
	reply, err := conn.RequestName("com.hello.world.Demo",
		dbus.NameFlagDoNotQueue)
	if err != nil {
		panic(err)
	}
	if reply != dbus.RequestNameReplyPrimaryOwner {
		fmt.Fprintln(os.Stderr, "name already taken")
		os.Exit(1)
	}
	f := foo{}
	conn.Export(f, "/com/hello/world/Demo", "com.hello.world.Demo")
	conn.Export(introspect.Introspectable(intro), "/com/hello/world/Demo",
		"org.freedesktop.DBus.Introspectable")
	fmt.Println("Listening on com.hello.world.Demo / /com/hello/world/Demo ...")
	select {}
}