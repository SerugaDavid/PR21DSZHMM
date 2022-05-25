import os
import pandas as pd
from collections import defaultdict


def main():
    directory = "csv"
    count = defaultdict(int)
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        print(f)
        if not os.path.isfile(f):
            continue
        try:
            file = pd.read_csv(f)
        except pd.errors.ParserError:
            continue
        count["lines"] += file.shape[0]
        count["columns"] += file.shape[1]
        count["files"] += 1
    print()
    print(count)


if __name__ == '__main__':
    main()
