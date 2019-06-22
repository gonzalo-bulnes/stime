# coding=utf-8

# An example timer that conveniently injects its time source dependency.

class Timer:
  """A timer the rings for 5 seconds when an alarm time is reached."""

  def __init__(self, time_source): # the time source is injected here, which is nice
    """Creates a new timer based on a time source.

    An adequate time source would typically be the time package
    from the standard library.

    Example:

            import time
            from timer import Timer

            reminder = Timer(time_source: time)

    """
    self.time_source = time_source

  def set_alarm(self, time):
    """Sets and alarm time using a timestamp."""
    self.alarm_time = time

  def is_ringing(self):
    """Whether the timer is ringing."""
    now = self.time_source.time() # depends on the current time!
    if self.alarm_time <= now <= self.alarm_time + 5:
      return True
    else:
      return False
