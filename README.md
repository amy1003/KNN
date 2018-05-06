# KNN

## Data processing
1. Place the netflix challenge data into dataset directory.
    If you already have them elsewhere, create a symbolic link. 
    In linux this is accomplished by:

    ```
    ln -s <path to um/> ./um
    ln -s <path to mu/> ./mu
    ```

2. Run the preprocessing script to split the data into `training`, 
   `validation`, `test` and `probe` sets.

    *Use Python 3 to ensure compatibility, although Python 2 should work too.*
    ```
    python preprocess.py
    ```