import argparse
from prog02_functions import dfs
from prog02_functions import isInterleaved
from prog02_functions import test

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", type=str, required=True, help="The path of input file.")
    args = parser.parse_args()
    filename = args.file_name
    #filename = "./prog02_input.txt"
    A = list()
    B = list()
    C = list()
    dp = [[[0] * 101] * 101] * 101
    complexity = 0
    with open(filename, "r") as f:
        for line in f:
            elements = line.split()
            A.append(elements[0])
            B.append(elements[1])
            C.append(elements[2])
    for i in range(len(A)):
        test(A[i], B[i], C[i])