#!/bin/bash

#pin_method="M0:0-3@M1:0-3@M2:0-3@M3:0-3" #valencia
pin_method="M0:0-5@M1:0-5@M2:0-5@M3:0-5" #quatchi
#pin_method="M0:0-7@M1:0-7@M2:0-7@M3:0-7M4:0-7@M5:0-7@M6:0-7@M7:0-7" #bulldozer

current_time=$(date "+%Y.%m.%d-%H.%M.%S")
for i in 6 12 22 #1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 #25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64
do
	for freq in 1000 100 10 1
	do
		for j in 1 2 3
		do
	 		# echo likwid-pin -q -c $pin_method ./$1 $i #echo likwid-pin -q ./$1 $i
	    echo env LD_LIBRARY_PATH=/cs/systems/home/yra3/repos/wiredtiger_use_rlu_extension/.libs:/cs/systems/home/yra3/repos/wiredtiger_use_rlu_extension/ext/compressors/snappy/.libs/:/cs/systems/home/yra3/repos/scalable-sync/rlu_relaxed_extension/lib ./db_bench_wiredtiger  --cache_size=134217728 --use_lsm=1 --use_existing_db=1 --db=/tmpfs/leveldb_wt_use_rlu --benchmarks=readseq --threads=$i --reads=20000000 --read_stats=1 --wait=$freq
	    
	    env LD_LIBRARY_PATH=/cs/systems/home/yra3/repos/wiredtiger_use_rlu_extension/.libs:/cs/systems/home/yra3/repos/wiredtiger_use_rlu_extension/ext/compressors/snappy/.libs/:/cs/systems/home/yra3/repos/scalable-sync/rlu_relaxed_extension/lib ./db_bench_wiredtiger  --cache_size=134217728 --use_lsm=1 --use_existing_db=1 --db=/tmpfs/leveldb_wt_use_rlu --benchmarks=readseq --threads=$i --reads=20000000 --read_stats=1 --wait=$freq >> logs/leveldb_rlu_${i}_${current_time}.log

	 		# likwid-pin -q -c $pin_method ./$1 $i >> logs/lpin_${1}_${current_time}.log
	   	done
	done
done