# Ask for a sentence
# Print the length of the sentence
# Ask for a filename (.txt)
# Write the sentence to the file
# Run the program from your command line

sentence = input('Enter a sentence: ')
sentenceLength = len(sentence)
print(sentenceLength)
fileName = input('Enter a file name: ')
fileName = f'{fileName}.txt'

with open(fileName, 'w') as f:
    f.write(sentence)
    f.close()

print(f"You've written {sentenceLength} characters to {fileName}")
