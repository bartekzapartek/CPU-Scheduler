from tests import test_low_burst_time
from tests import test_medium_burst_time

def test_different_burst_time():
   test_low_burst_time()
   test_medium_burst_time()

def run():
   test_different_burst_time()

run()
