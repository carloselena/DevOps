#width = 17
#height = 12.0

#type(width)

#x = int(input("Enter an integer number: "))

#if x < 0:
    #pass    # need to handle negative values!!!


#text = "X-DSPAM-Confidence:    0.8475"

#num = text.find("0")
#posn = num
#whnum = float(text[num:])
#print(whnum)

#last = text[-2]
#print(last)

#https://docs.python.org/library/stdtypes.html#string-methods

#https://docs.python.org/library/stdtypes.html#string-methods

#docs.python.org/library/stdtypes.html#common-sequence-operations

#fhand = open('mbox-short.txt')
#inp = fhand.read()
#print(len(inp))
#print(len(inp))


#for line in fhand:
 #   line = line.rstrip()
  #  if line.startswith("From: "):
   #     print(line)

#for line in fhand:
 #   line = line.rstrip()
  #  if line.find('@uct.ac.za') == -1:
   #     continue
    #print(line)

#New!!!

#fname = input('Enter the file name: ')

#try:
 #   fhand = open(fname)
  #  count = 0
   # for line in fhand:
    #    if line.startswith('Subject:'):
     #       count = count + 1
    #print('There were', count, 'subject lines in', fname)
#except:
 #   print('Error, file not found. Please, enter a valid file name.')


#If the file already exists, opening it in write mode clears out
#the old data and starts fresh, so be careful!
#If the file doesn’t exist, a new one is created.

#s = '1 2\t 3\n 4'
#print(s)
#print(repr(s))










#print('Hello from a file')

#x = 5
#print (x)

#y = [5, 6, 3.5, 45]

#def xy(y):
    #for y in y:
        #print(y)

#xy(y)

#xlist = list()

#while True:
   # inp = input('Enter a number: ')
  #  if inp == 'done': break
 #   value = float(inp)
#    xlist.append(value)

#average = sum(xlist)/len(xlist)
#print(average)

fname = input('Enter a file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[2])


        
    
