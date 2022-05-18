#!/bin/bash
for i in `seq 1 20`;
do
	./a.out > ./ftest/frantst$i
done

for i in ./ftest/*;
do
	$lines = cat $i | wc -l
	cat $i | head -n$((lines - 1)) > $i.i
	cat $i | tail -n1 > $i.o
	rm $i
done
