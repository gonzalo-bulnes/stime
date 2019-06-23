<p align='center'><img width="128" src='./vendor/noto-emoji-owl.png' alt="🦉 An owl emoji"/></p>
<h1 align='center'>Simulated Time</h1>

<p align="center">A testing (and partial) replacement for Python's <code>time</code> package, for fully-controlled time-dependent tests.</p>
<p align="center"><a href="https://pypi.org/project/stime"><img alt="PyPI" src="https://img.shields.io/pypi/v/stime.svg" /></a></p>

<br /><br />

Testing functions that depend on time is always tricky, and can take long. To save time and avoid relying on `time.sleep()`, this package allows to fast-forward time arbitrarily.

It implements the functions `stime.time()` and `stime.monotonic()`.

<br />

> **Note**: This package in not meant to replace [`time`][time] in production! Only in testing environments!

  [time]: https://docs.python.org/3/library/time.html

Usage
-----

The idea is to make your code to use `stime.test()` instead of `time.test()` while it is being tested.

Ideally, the code you want to test is receiving a time source through [dependency injection][di], like the `Timer` class in the example below.

  [di]: https://www.jamesshore.com/Blog/Dependency-Injection-Demystified.html

If the code you are testing is not using dependency injection, it is likely that you can still override the time function in your tests. That is less elegant, but can be a fair trade-off to avoid having its test suite rely on `time.sleep()`.

Once your code is using `stime`, you can precisely control the output of `stime.time()` (or `stime.monotonic()`) using `stime.reset()` and `stime.tick()`:

- **`tick(n)`**: increments the current time by `n` seconds (e.g. `1.3` seconds)
- **`reset(t)`**: (re-)sets the current time to the timestamp `t` (e.g. `1561120200`)

### Example

Find the full code for this example in [`examples/timer`](./examples/timer)!

```python
# test_timer.py

import unittest
import stime # ①
from timer import Timer # your package with time-dependent functions to be tested

class TestTimer(unittest.TestCase):

    def test_timer_rings_for_five_seconds_starting_at_alarm_time(self):
        # create a new timer using stime as a time source
        cooking_timer = Timer(time_source=stime)
        cooking_timer.set_alarm(1561120200) # Unix timestamp for 21 June 2019 around noon

        stime.reset(1561120199) # ② a second before alarm time
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, False, "expected the timer NOT to ring before alarm time")

        stime.reset(1561120200) # ③ exactly alarm time
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, True, "expected the timer to ring at alarm time")

        stime.tick(5) # ④ 5 seconds after alarm time
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, True, "expected the timer to be ringing 5 seconds after alarm time")

        stime.tick() # ⑤ add 1 more second
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, False, "expected the timer NOT to be ringing 6 seconds after alarm time")

# [...]
```

- ① Import `stime` where you would have imported `time` if it wasn't testing.
- ② Set the current time to whatever is convenient...
- ③ Reset it as often as needed...
- ④ Fast-forward when convenient...
- ⑤ or progress one second at a time!

Development
-----------

### Getting started

Optionally, create a virtual environment for this project and activate it.

```bash
python -m venv venv # assuming Python 3
. venv/bin/activate
```

Then do your thing!

```bash
# run the test suite:
python test_stime.py

# once you're done deactivate the virtual environment if you use one:
deactivate
```

### Release

```bash
# Install the latest setuptools and wheel (I put them in the same virtual environment)
pip install --upgrade setuptools wheel

# Update the package version number and tag it:
vim setup.py
git tag -a 'v1.0.0' -m 'Initial release'
git push origin master --tags

# Build the distribution files
make build

# And upload them to PyPI
make upload_to_pypi
```

Contributing
------------

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-e7359e.svg?style=popout)](http://makeapullrequest.com)
![Code Review Welcome](https://img.shields.io/badge/code%20review-welcome-e7359e.svg?style=popout)

I am [learning Python](https://github.com/gonzalo-bulnes/kata-python-web-app)! 🎉

This is the first package I publish and I did it very much to figure out how things work. That's to say that I'd love to hear your thoughts, maybe we can learn something together : )

Whether it is your first pull request or your 100th, the [contributing guidelines][contributing] are here to help you get started!

Please note that by participating in this project, you agree to abide by its [code of conduct]. That is true for pull requests, and also when participating in issues.

  [contributing]: ./CONTRIBUTING.md
  [code of conduct]: ./CODE_OF_CONDUCT.md

Credits
-------

The owl emoji in the header was rendered from an SVG that belongs to Google and [was published under the Apache License v2.0 as part of Noto Emoji](https://github.com/googlei18n/noto-emoji).

License
-------

    stime
    Copyright (C) 2019 Gonzalo Bulnes Guilpain

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
