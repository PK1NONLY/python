# writing   to the file sample.txt file will create if not exist.

fw = open('sample.txt', 'w')
fw.write('Writing some stuff in my text file\n')
fw.write('I like python\n')
fw.close()

# reading from sample.txt file
fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()