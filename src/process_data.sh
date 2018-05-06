#! /bin/sh

./process_data process um/base.dta um/base.bin
./process_data validate um/base.dta um/base.bin

./process_data process um/valid.dta um/valid.bin
./process_data validate um/valid.dta um/valid.bin

./process_data process um/test.dta um/test.bin
./process_data validate um/test.dta um/test.bin

./process_data process um/probe.dta um/probe.bin
./process_data validate um/probe.dta um/probe.bin

./process_data process um/qual.dta um/qual.bin --no-ratings
./process_data validate um/qual.dta um/qual.bin --no-ratings
