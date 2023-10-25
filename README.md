# Alicat
========================================

## Documentation
------------
* [Alicat Serial Commands](https://www.alicat.com/wp-content/documents/Alicat-Serial-Primer.pdf)
* [General Alicat Information](https://www.alicat.com/using-your-alicat/how-to-issue-serial-commands/)

## API
------------
These are the methods currently available in Module-Alicat.py

### Initialization
Initialize the Pressure Meter object:

      >>> pressure_meter = alicat_pressure()

Default:

      >>> alicat_pressure(port="/dev/tty.usbserial-AU0585NK", baudrate=19200)

### Start the value stream:


