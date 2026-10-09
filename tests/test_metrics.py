import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from experiment_metrics import compare,wilson
class MetricsTests(unittest.TestCase):
    def test_small_sample_does_not_prove_improvement(self):
        lo,hi=compare(10,100,15,100)['difference_95_interval']
        self.assertLess(lo,0);self.assertGreater(hi,0)
    def test_swap_symmetry(self):
        a=compare(20,100,40,120);b=compare(40,120,20,100)
        self.assertAlmostEqual(a['difference'],-b['difference'])
        self.assertAlmostEqual(a['difference_95_interval'][0],-b['difference_95_interval'][1])
    def test_extremes(self):
        self.assertGreater(wilson(0,20)[1],0)
        self.assertLess(wilson(20,20)[0],1)
    def test_invalid_denominator(self):
        for a,n in [(1,0),(11,10),(-1,10),(1.5,10),(True,10)]:
            with self.assertRaises(ValueError):wilson(a,n)
if __name__=='__main__':unittest.main()
