#!/usr/bin/env python3

# Splits data into training, validation, test and probe sets
data_path = 'dataset/um/'
with open(data_path + 'all.dta', 'r') as dat, open(data_path + 'all.idx', 'r') as idx:
    with open(data_path + 'base.dta', 'w') as base, open(data_path + 'valid.dta', 'w') as valid, \
            open(data_path + 'test.dta', 'w') as test, open(data_path + 'probe.dta', 'w') as probe:
        for d, i in zip(dat, idx):
            fold = i[0]
            if fold == '1':
                base.write(d)
            elif fold == '2':
                valid.write(d)
            elif fold == '3':
                test.write(d)
            elif fold == '4':
                probe.write(d)
