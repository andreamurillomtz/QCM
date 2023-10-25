# Alicat

## Documentation
* [Alicat Serial Commands](https://www.alicat.com/wp-content/documents/Alicat-Serial-Primer.pdf)
* [General Alicat Information](https://www.alicat.com/using-your-alicat/how-to-issue-serial-commands/)

## API Flow Meter

These are the methods currently available in Module-Alicat.py

### Initialization
Initialize the Pressure Meter object:
```
    >>> flow_meter = alicat_flow()
```
Default:
```
    >>> alicat_flow(port="/dev/tty.usbserial-AU0585NK", baudrate=19200)
```
### Start value stream
Call module:
```
    >>> flow_meter.start_stream(unit_id) 
```
### Stop value stream
Call module:
```
    >>> flow_meter.stop_stream(unit_id)
```
### Poll Data
Call module:
```   
    >>> flow_meter.poll_data(unit_id)
```
### Tare
Call module:
```
    >>> flow_meter.tare(unit_id) 
```
### Available Gases
Call module:
```
    >>> flow_meter.available_gases(unit_id) 
```
### Change Gas
Call module:
```
    >>> flow_meter.change_gas(unit_id)
```
### Read Stream
Call module:
```
    >>> flow_meter.read_stream(unit_id) 
```
### Change Unit ID
Call module:
```
    >>> flow_meter.change_unit_id(unit_id)
````
### Baudrate
Call module:
```
    >>> flow_meter.baud_rate(unit_id)
````
---------------------
## API Pressure meter

These are the methods currently available in Module-Alicat.py

### Initialization
Initialize the Pressure Meter object:
```
    >>> presure_meter = alicat_pressure()
```
Default:
```
    >>> alicat_pressure(port="/dev/tty.usbserial-AU0585NK", baudrate=19200)
```
### Start value stream
Call module:
```
    >>> pressure_meter.start_stream(unit_id) 
```
### Stop value stream
Call module:
```
    >>> pressure_meter.stop_stream(unit_id)
```
### Poll Data
Call module:
```   
    >>> pressure_meter.poll_data(unit_id)
```
### Tare
Call module:
```
    >>> pressure_meter.tare(unit_id) 
```
### Available Gases
Call module:
```
    >>> pressure_meter.available_gases(unit_id) 
```
### Change Gas
Call module:
```
    >>> pressure_meter.change_gas(unit_id)
```
### Read Stream
Call module:
```
    >>> pressure_meter.read_stream(unit_id) 
```
### Change Unit ID
Call module:
```
    >>> pressure_meter.change_unit_id(unit_id)
````
### Baudrate
Call module:
```
    >>> pressure_meter.baud_rate(unit_id)
````












