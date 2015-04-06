import random
import os.path

PATH = './word_master.txt'

if os.path.exists(PATH):
	f = open('word_master.txt', 'r')	# opening the file
else:
	print "File 'word_master.txt' does not exist."
	quit()

words = []
revise = []

for line in f:
	line = line[0:len(line) - 2]	# to remove extra characters '/r/n'
	words.append(line)

f.close()

print "Welcome to Word Master! Test your vocabulary."
print "After the word appears on the screen,"
print "Type 'y' if you know the meaning, 'n' if you don't and 'q' to quit"
print "(Type without quotes)"
print "=================================================================="
print "Let's begin!"
print

while len(words) > 0:
	rand = random.randrange(len(words))
	print words[rand]
	
	ans = raw_input()
	
	if ans == 'y':
		del words[rand]
	elif ans == 'n':
		revise.append(words[rand])
		del words[rand]
	elif ans == 'q':
		break
	else:
		print "What's that? Try again."

print
print "The End"
print "List of words you need to revise:"
print

for x in revise:
	print x

print
save = raw_input("Do you want to save these words in a file (y/n)? ")

if save == 'y':
	fi = open('revision.txt', 'w+')
	
	for item in revise:
		fi.write("%s\n" % item)
	
	print "Done! Words saved in 'revision.txt'"
else:
	print "Fine."
