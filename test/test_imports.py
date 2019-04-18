import unittest


class TestImports(unittest.TestCase):

    def test_imports(self):
        from psr_formats import DADAFile, DataFile
        self.assertTrue(DADAFile.__name__ == "DADAFile")
        self.assertTrue(DataFile.__name__ == "DataFile")


if __name__ == "__main__":
    unittest.main()
