#!/bin/bash

while read line; do
    echo $line
    ./run_qualm_bench.sh $line 60 1
done < qualm_circuits_full.txt
