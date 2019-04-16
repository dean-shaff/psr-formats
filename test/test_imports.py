import unittest


class TestImports(unittest.TestCase):

    def test_imports(self):
        from psr_formats import DADAFile
        self.assertTrue(DADAFile.__name__ == "DADAFile")


if __name__ == "__main__":
    unittest.main()
