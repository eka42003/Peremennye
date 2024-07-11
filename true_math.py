import math
def divide(one_, two_):
    if two_ == 0:
        return math.inf
    else:
        return one_/two_
if __name__ == '__main__':
    print (divide(30,0))