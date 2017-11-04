import os
import csv
from random import randint

if __name__ == "__main__":
    if os.path.exists('data/numbers.csv'):
        with open('data/numbers.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            for i in range(1000):
                arr = []
                maxn = 0
                for i in range(10):
                    num = randint(0, 9)
                    if num > maxn:
                        maxn = num
                    arr.append(num)
                arr.append(maxn)
                writer.writerow(arr)
