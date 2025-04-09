#!/bin/zsh
for i in `seq 1 50`;
 do
	./clientmiro.py out a
	sleep 1
	./clientmiro.py in a
	sleep 1
done
