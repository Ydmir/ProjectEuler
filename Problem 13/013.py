print(str(sum([int(numberString[0:20]) for numberString in open("data_013.txt").read().split('\n')]))[0:10])