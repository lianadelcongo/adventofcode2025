from collections.abc import Callable


def load_file(filename: str)->list[str]:
    with open(filename) as my_file:
        return my_file.readlines()
    return []

def isRepeatedNumber(num:int)->bool:
    rep = str(num)
    length = len(rep)
    if length < 2:
        return False
    for size in range(1, length//2+1):
        if length % size != 0:
            continue
        pattern = rep[0:size]
        for st in range(size, length, size):
            if rep[st:st+size] != pattern:
                break
        else:
            return True
    return False        


def isRepeatedTwiceNumber(num:int)->bool:
    rep = str(num)
    if len(rep) % 2 == 0 and rep[0:len(rep)//2] == rep[len(rep)//2:]:
        return True
    return False

def checkRange(start:int, end:int, fn: Callable[[int], int])->int:
    s = 0
    for i in range(start,end+1):
        if fn(i):
            s+=i
    return s

def compute(file:str, fn: Callable[[int], int])->int:
    line = load_file(file)[0]
    s = 0
    for interval in line.split(","):
        (start,end) = interval.split("-")
        s += checkRange(int(start), int(end), fn)
    return s

if __name__ == "__main__":
    print(f"star1: {compute('day2/example.txt', isRepeatedTwiceNumber)}")
    print(f"star1: {compute('day2/data.txt', isRepeatedTwiceNumber)}")
    print(f"star2: {compute('day2/example.txt', isRepeatedNumber)}")
    print(f"star2: {compute('day2/data.txt', isRepeatedNumber)}")