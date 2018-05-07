
import pyreclab
import argparse

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
                               dlmchar=b'\s',
                               header=False,
                               usercol=0,
                               itemcol=1,
                               ratingcol=3)
    else:
        obj = pyreclab.UserAvg(dataset=args.train,
                               dlmchar=b'\s',
                               header=False,
                               usercol=0,
                               itemcol=1,
                               ratingcol=3)

    # Train
    knn = 10
    similarity = 'cosine'

    if (args.code_test == 0):
        obj.train(knn, similarity)
    else:
        obj.train()

    # Predict
    with open(args.qual, 'r') as qual:
        with open(args.output, 'w') as pred:
            for line in qual:
                x = line.split(' ')
                r = obj.predict(x[0], x[1])
                pred.write(str(r) + "\n")
