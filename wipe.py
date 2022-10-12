import random


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


if __name__ == "__main__":
    print("File path:")
    pathtowipe = input()
    corruptFile(pathtowipe)
