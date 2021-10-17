import time
from threading import Event, Thread


class RepeatedTimer:

    """Repeat `function` every `interval` seconds."""

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.event = Event()
        self.thread = Thread(target=self._target)
        self.thread.start()

    def _target(self):
        while not self.event.is_set():
            self.function(*self.args, **self.kwargs)
            time.sleep(self.interval)

    def stop(self):
        self.event.set()
        self.thread.join()
