while read p; do
  cat chat.txt |grep "] $p" |grep '\['| cut -d']' -f2-|cut -d":" -f2- > ./temp/out."$p".txt
done <namen.txt
