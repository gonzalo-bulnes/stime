# coding=utf-8

import unittest
import stime
from timer import Timer # your package with time-dependent functions to be tested

class TestTimer(unittest.TestCase):

    def test_timer_does_not_ring_before_set_time(self):
        # create a new timer using stime as a time source
        cooking_timer = Timer(time_source=stime)
        cooking_timer.set_alarm(1561120200) # Unix timestamp for 21 June 2019 around noon

        stime.reset(1561120199) # a second before alarm time
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, False, "expected the timer NOT to ring before alarm time")

    def test_timer_rings_at_set_time(self):
        # create a new timer using stime as a time source
        cooking_timer = Timer(time_source=stime)
        cooking_timer.set_alarm(1561120200) # Unix timestamp for 21 June 2019 around noon

        stime.reset(1561120200) # exactly alarm time
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, True, "expected the timer to ring at alarm time")

    def test_timer_rings_for_five_seconds(self):
        # create a new timer using stime as a time source
        cooking_timer = Timer(time_source=stime)
        cooking_timer.set_alarm(1561120200) # Unix timestamp for 21 June 2019 around noon

        stime.reset(1561120205) # 5 seconds after alarm time
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, True, "expected the timer to be ringing 5 seconds after alarm time")

        stime.tick() # add 1 more second
        is_ringing = cooking_timer.is_ringing() # calls stime.time() because it is the timer time_source
        self.assertEqual(is_ringing, False, "expected the timer NOT to be ringing 6 seconds after alarm time")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTimer)
    unittest.TextTestRunner(verbosity=2).run(suite)
