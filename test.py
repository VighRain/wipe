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

    def test2DoesFileExistAfterWiping(self):
        print("File wipe test")
        pathtowipe = input()
        isWiped = wipe.wipeFile(pathtowipe)
        self.assertEqual(isWiped, True)

    def test3DoesDirectoryExistAfterWiping(self):
        print("Directory wipe test")
        pathtowipe = input()
        isWiped = wipe.wipeDir(pathtowipe)
        self.assertEqual(isWiped, True)


if __name__ == "__main__":
    unittest.main()
