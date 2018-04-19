__author__ = "Jacopo De Luca"
__version__ = "1.0.0"

import threading
import time
import sys


class ProgressBar(threading.Thread):
    def __init__(self, message, cmessage=str()):
        super(ProgressBar, self).__init__()
        self.message = message
        self.cmessage = cmessage
        self.stop = False

    def cancelProgress(self):
        self.stop = True
        while self.isAlive():
            time.sleep(0.20)

    def _printAnimation(self, defSeq="\\-/|"):
        for cur in defSeq:
            sys.stdout.write(cur + "\b")
            sys.stdout.flush()
            time.sleep(0.150)


class IndeterminateProgress(ProgressBar):
    def run(self):
        sys.stdout.write(self.message + ".... ")
        sys.stdout.flush()
        while not self.stop:
            self._printAnimation()
        sys.stdout.write(" %s\n" % self.cmessage)
        sys.stdout.flush()


class DeterminateProgress(ProgressBar):
    def __init__(self, message, cmessage=str(), progchr="#", width=10):
        super(DeterminateProgress, self).__init__(message, cmessage)
        self._progchr = progchr
        self._width = width
        self._progress = 0
        self._max = 100

    def run(self):
        while not self.stop:
            curr_prog = self._progchr * int(self._progress * self._width / self._max)
            sys.stdout.write("\r%s [%s" % (self.message, curr_prog))
            sys.stdout.flush()
            if self._progress == self._max:
                print("] %s" % self.cmessage)
                return
            self._printAnimation()
        return

    def setMax(self, value):
        self._max = value

    @property
    def getMax(self):
        return self._max

    @property
    def getProgress(self):
        return self._progress

    @property
    def getChr(self):
        return self._progchr

    def incProgress(self, value):
        if not self.isAlive():
            raise RuntimeError("Call .start() before .incProgress()")
        self._progress += value

    def sync(self):
        while self.isAlive():
            time.sleep(0.20)
