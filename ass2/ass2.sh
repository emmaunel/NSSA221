#!/bin/bash

FILE="user.csv"
tmp="/tmp/user.csv"
NEW_FILE="$(tail +2 $FILE > $tmp)"
IFS=","
head="$(head -n 1 $FILE)"
IFS=', ' read -r -a head_array <<< "$head"
head_length=${#head_array[@]}

main(){
    while read LINE; do
            IFS=', ' read -r -a array <<< "$LINE"
            line_length=${#array[@]}

            for (( i = 0 ; i < $line_length - 1 ; i++)); do
                echo "${head_array[$i]} [$i]: ${array[$i]}"
                if[["${array[$i]}" = " "]];
                    echo "hi"
                fi
            done
            echo " "

    done < $tmp
}


main