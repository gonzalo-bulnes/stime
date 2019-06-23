Testing a Timer — Demo
======================

Demonstrates how to test a simple timer without spending `time.sleep()`.

## Installation

Optionally, create a virtual environment for this example and activate it.

```bash
python -m venv timer_venv # assuming Python 3
. timer_venv/bin/activate
```

Then install the example dependencies (only `stime` in fact):

```bash
pip install -r requirements.txt
```

## Usage

```bash
# activate the virtual environment if you use one:
. timer_venv/bin/activate

# run the example test suite:
python test_timer.py

# once you're done deactivate the virtual environment if you use one:
deactivate
```
