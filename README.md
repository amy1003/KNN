# KNN

## Requirement


## Data processing
1. Place the netflix challenge data into dataset directory.
    
If you already have them elsewhere, create a symbolic link. 
In linux this is accomplished by (from the dataset directory):

    ```
    ln -s <path to um/> ./um
    ln -s <path to mu/> ./mu
    ```

2. Run the preprocessing script to split the data into `training`, 
`validation`, `test` and `probe` sets.

*Use Python 3 to ensure compatibility, although Python 2 should work too.*

    ```
    python src/preprocess.py
    ```

## Train and predict

To train and predict:

    '''
    python src/KNN.py -t dataset/um/base.dta -q dataset/um/qual.dta -o result/output.dta
    '''

To test code on UserAvg:

    '''
    python src/KNN.py -t dataset/um/base.dta -q dataset/um/qual.dta -o result/output.dta --code_test 1
    '''
Options:
* -t (--train) `<File path>`: Required
    Training data file path.
* -q (--qual) `<File path>`: Required
    Qual data file path.
* -o (--ouput) `<File path>`: Required
    Output data file path.
* --code_test  `<int>`: Optional
    Test code tag. 
    