#!/bin/bash

while read line; do
    echo $line
    ./run_qulm_bench.sh $line 60 1
done < qalm_circuits_full.txt
