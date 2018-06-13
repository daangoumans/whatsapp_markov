# whatsapp_markov
Using your whatsapp export to generate messages


EXPORT Whatsapp in format like: [dd-mm-yy hh:mm:ss] name: message
  
RUN: cat _chat.txt |grep '\['| cut -d']' -f2|cut -d":" -f1|grep -v 'gewijzigd' | sort | uniq >namen.txt

CHECK THIS namen.txt file

MAKE: ./temp directory

RUN: extract_chats.sh

RUN python3 markov_text_sim.py -i temp/<inputfile> -n <amount>
