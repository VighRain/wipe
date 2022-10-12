import unittest
import wipe

class testWipe(unittest.TestCase):

    def test1WasFileCorrupted(self):
        print("File corruption test")
        pathtowipe = input()
        with open(pathtowipe, 'r') as f:
            contents = f.read()
        corrupted_contents = wipe.corruptFile(pathtowipe)
        self.assertNotEqual(contents, corrupted_contents)


if __name__ == "__main__":
    unittest.main()
