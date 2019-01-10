import unittest
import os


def all_tests():
    suite = unittest.TestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern='test_*.py',
        top_level_dir=None
    )
    return suite


def run():
    unittest.TextTestRunner(verbosity=2).run(all_tests())


if __name__ == '__main__':
    run()
