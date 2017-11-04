import csv
from random import randint

if __name__ == "__main__":
    if os.path.exists('data/numbers.csv'):
        with open('data/numbers.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            for i in range(300):
                arr = []
                num = randint(0, 9)
                arr.append(num)
                arr.append(num)
                writer.writerow(arr)
