#!/bin/bash

# when passing path as argument in bash, please use single quotes
# to avoid backslash problems. Ex: 'C:\Users\some-folder'
# find all files under given directory and putting them into an array
lista_arquivos(){
	# empty array
	vector=()
	# aux var to receive argument
	var1=$1
	# replace '\' with '/'
	var="${var1//\\//}"
	#recursive loop to find and read all files
	while read -d $'\0' file; do
		vector+=($file)
	done < <(find $var -type f -print0)
}

ler(){
	for i in ${vector[@]}; do
		insere_texto $i "$1"
	done
}

# given 2 arguments ($1 file path, $2 content to insert)
# this function writes the content at the end of the file
insere_texto(){
	echo "$2" >> $1
}
