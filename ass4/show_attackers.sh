#!/bin/bash

# Ayobami Adewale --> Script 4(easy)
if [ -f "$1" ]; then
      cat $1 | grep Failed > /tmp/filter
else
      echo "Cannot open log file: $1"
      exit 1
fi

# Get all the ip seperately and saves it temporarly
cat /tmp/filter | cut -d " " -f 11 | sort -u | grep '[0-9].[0-9].' > /tmp/ips

#CSV Header
printf '%s\n' Count IP Location | paste -sd ',' >> logs.csv

# Parse the ips and location into a csv file
while read line; do
      # Gets the number of times an ip appears
 	num=$(grep -o $line /tmp/filter | wc -l)
      # if less than 10 ignore, else get the location and save it the csv
     	if [ $num -lt 10 ]; then
            true
      else
            location=$(geoiplookup $line | cut -d " " -f 5,6)
            printf '%s\n' $num $line $location | paste -sd ',' >> logs.csv
      fi
done < /tmp/ips

#delete temp files and displaying results
rm /tmp/filter
rm /tmp/ips
cat logs.csv
