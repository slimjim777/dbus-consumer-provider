# dbus - consumer/provider example

This demonstrates calling a method on another application using dbus. The provider is
written in Go, and the consumer is in python.

Build each application using snapcraft and connect the interfaces:

```
sudo snap connect test-consumer:foo-svc test-provider:dbus-svc
```
