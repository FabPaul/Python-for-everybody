"""
program that opens a file, splits the words, count them and return the most frequent word with its count
"""
while True:
    name = input("Please enter file name: ")
    try:
        if name:
            with open(name) as handle:
                counts = dict()
                for line in handle:
                    words = line.split()

                    for word in words:
                        counts[word] = counts.get(word, 0) + 1

            bigcount = None
            bigword = None

            for word, count in counts.items():
                if bigcount is None or count > bigcount:
                    bigword = word
                    bigcount = count

            print(f"The most frequent word is {bigword} and the count is {bigcount}")
        break
    except Exception:
        print("Please enter a valid file name")