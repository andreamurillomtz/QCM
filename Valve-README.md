# Alicat

## Documentation


## API Flow Meter

These are the methods currently available in Module-Valve.py

### Initialization
Initialize the Pressure Meter object:
```
    >>> valve_controller = valves()
```
Default:
```
    >>> valves(port="/dev/tty.usbmodem12201", baudrate=9600, valves_available=["1", "2", "3", "4"], valve_status=["0", "0", "0", "0", "0"] )
```
### Open Valve
call module:
```
    >>> valve_controller.open_valve(number_of_modified_valve) 
```
### Close Valve
call module:
```
    >>> valve_controller.close_valve(number_of_modified_valve) 
```
### Stop
call module:
```
    >>> valve_controller.stop() 
`
