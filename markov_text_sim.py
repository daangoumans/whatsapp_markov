#!/usr/bin/python3
import sys, getopt
import numpy as np

'''
EXPORT Whatsapp in format like: [dd-mm-yy hh:mm:ss] <name>: <message>
RUN: cat _chat.txt |grep '\['| cut -d']' -f2|cut -d":" -f1|grep -v 'gewijzigd' | sort | uniq >namen.txt
CHECK namen.txt file
MAKE: temp directory
RUN: extract_chats.sh
RUN python3 markov_text_sim.py -i <inputfile> -n <amount>
'''
def print_markov(file,amount):
    text_set = open(file, encoding='utf8').read()

    corpus = text_set.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    for i in range(int(amount)):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    print(' '.join(chain))

def main(argv):
   inputfile = ''
   namount = ''
   try:
      opts, args = getopt.getopt(argv,"hi:n:",["ifile=","namount="])
   except getopt.GetoptError:
      print ('markov.py -i <inputfile> -n <amount>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
          print ('markov.py -i <inputfile> -n <amount>')
          print ()
          print ('please use the bash "extract_chats.sh" file first')
          print ('this is used to generate sub-messagelists for each person')
          sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-n", "--namount"):
         namount = arg
   #print ('Input file is: ', inputfile)
   #print ('Amount is: ', namount)
   print_markov(inputfile, namount)

if __name__ == "__main__":
   main(sys.argv[1:])
