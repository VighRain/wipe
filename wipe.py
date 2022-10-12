import random
import os
import shutil


def corruptFile(pathtowipe):
    with open(pathtowipe, 'r') as f:
        contents = f.read()
        for i in range(0, len(contents)):
            insert_at = random.randint(0, len(contents))
            contents = contents[:insert_at] + '#' + contents[insert_at:]
        f.close()
    with open(pathtowipe, 'w') as f:
        f.write(contents)
        f.close()
    return contents


def wipeFile(pathtowipe):
    if os.path.exists(pathtowipe):
        os.remove(pathtowipe)
        return True
    else:
        return False


def wipeDir(pathtowipe):
    if os.path.exists(pathtowipe):
        for filename in os.listdir(pathtowipe):
            corruptFile(os.path.join(pathtowipe, filename))
        shutil.rmtree(pathtowipe)
        return True
    else:
        return False


if __name__ == "__main__":
    print("File/directory path:")
    pathtowipe = input()
    if os.path.isfile(pathtowipe):
        corruptFile(pathtowipe)
        wipeFile(pathtowipe)
    elif os.path.isdir(pathtowipe):
        wipeDir(pathtowipe)
