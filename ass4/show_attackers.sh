#!/bin/bash

file=$1
#check if geoip is install, if not install it

if [ -f "$file" ]; then
      echo "Exists"
      cat $file | grep Failed > /tmp/filter
else
      echo "Cannot open log file: $file"
      exit 1
fi

# need to get all the ip seperately
cat /tmp/filter | cut -d " " -f 11 | sort -u | grep '[0-9].[0-9].' > /tmp/ips

#grep -o 'ip' test | wc -l
while read line; do
	 echo $line;
 	 num=$(grep -o $line /tmp/filter | wc -l)
     	 [ $num -lt 10 ] && echo "ignore for now" || geoiplookup $line | cut -d " " -f 5
done < /tmp/ips

echo "Don't forget to delete /tmp/filter and /tmp/ips"
