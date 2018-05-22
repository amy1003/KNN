
import pyreclab
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='KNN')
    parser.add_argument('--train', '-t', required=True, type=str,
                        help='input training data')
    parser.add_argument('--qual', '-q', required=True, type=str,
                        help='input qual data')
    parser.add_argument('--output', '-o', required=True, type=str,
                        help='output file path')
    parser.add_argument('--code_test', default=0, type=int,
                        help='test code using UserAvg')
    args = parser.parse_args()

    if (args.code_test == 0):
        obj = pyreclab.UserKnn(dataset=args.train,
                               dlmchar=b' ',
                               header=False,
                               usercol=0,
                               itemcol=1,
                               ratingcol=3)
    else:
        obj = pyreclab.UserAvg(dataset=args.train,
                               dlmchar=b' ',
                               header=False,
                               usercol=0,
                               itemcol=1,
                               ratingcol=3)

    # Train
    print("Training starting")
    knn = 100
    similarity = 'pearson'

    if (args.code_test == 0):
        start = time.clock()
        print("obj.train knn, similarity")
        obj.train(knn, similarity)
        end = time.clock()
        print( 'training time: ' + str( end - start ) )
    else:
        start = time.clock()
        print("obj.train")
        obj.train()
        end = time.clock()
        print( 'training time: ' + str( end - start ) )

    # Test
    print("Testing starting")
    start = time.clock()
    predlist, mae, rmse = obj.test( input_file = 'dataset/um/valid.dta',
                                    dlmchar = b' ',
                                    header = False,
                                    usercol = 0,
                                    itemcol = 1,
                                    ratingcol = 3,
                                    output_file = 'result/test_predictions.dta')
    start = time.clock()
    print( 'testing time: ' + str( end - start ) )

    print( 'MAE: ' + str( mae ) )
    print( 'RMSE: ' + str( rmse ) )

    # Predict
    print("Predictions starting")
    with open(args.qual, 'r') as qual:
        with open(args.output, 'w') as pred:
            for line in qual:
                print("Predicting...")
                x = line.split(' ')
                r = obj.predict(x[0], x[1])
                pred.write(str(r) + "\n")
