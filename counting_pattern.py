"""
write a code that takes a line of text, splits it, returns the split text as a dictionray,
showing the frequency of occurency of each word

A sample text it can take:

the murderer that murdered the mother of the previous murderer's mother who murdered the mother of the other murderer's mother has murdered the mother of the mother that murdered her mother after she murdered the mother of the murderer who intended to murder her mother and stopped him from murdering the mother who almost murdered her mother
"""

count = dict()
line = input("Please enter some text. Hit Enter when you are done: ")
words = line.split()

print("Words:", words)
for word in words:
    count[word] = count.get(word, 0) + 1
print("Count", count)
