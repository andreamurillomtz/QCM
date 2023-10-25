# Alicat

## Documentation
* [Alicat Serial Commands](https://www.alicat.com/wp-content/documents/Alicat-Serial-Primer.pdf)
* [General Alicat Information](https://www.alicat.com/using-your-alicat/how-to-issue-serial-commands/)

## API

These are the methods currently available in Module-Alicat.py

### Initialization
Initialize the Pressure Meter object:

    >>> pressure_meter = alicat_pressure()

Default:

    >>> alicat_pressure(port="/dev/tty.usbserial-AU0585NK", baudrate=19200)

### Start value stream
Call module:
    >>> pressure_meter.start_stream(unit_id) 

### Stop value stream
Call module:
    >>> pressure_meter.stop_stream(unit_id)

### Poll Data
Call module:
    >>> pressure_meter.poll_data(unit_id)

### Start value stream
Call module:
    >>> pressure_meter.start_stream(unit_id) 

### Tare
Call module:
    >>> pressure_meter.tare(unit_id) 








