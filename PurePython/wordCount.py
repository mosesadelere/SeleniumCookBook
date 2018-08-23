def wordCount(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        #print("This file '" + filename + "' was not found")
        pass
    else:
        words = content.split()
        counts = len(words)
        print("This file '" + filename + "' has " + str(counts) + " words.")

filenames = ['guestfile.txt', 'learning_python.txt', 'test.txt']
for filename in filenames:
    wordCount(filename)
