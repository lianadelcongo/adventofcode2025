
def load_file(filename: str)->list[str]:
    with open(filename) as my_file:
        return my_file.readlines()
    return []

def max_num(line:str)->int:
    d = 0
    for i in range(0,len(line)-1):
        if line[i]>line[d]:
            d = i
    u = d + 1
    for i in range(u,len(line)):
        if line[i]>line[u]:
            u = i
    return 10*int(line[d]) + int(line[u])

def max_num_recursive(nums:list[int], pending:int)->int:
    if pending == 1:
        return max(nums)
    p = 0
    for i in range(0,len(nums)-pending+1):
        if nums[i]>nums[p]:
            p = i
    
    return (10**(pending-1))*nums[p]+max_num_recursive(nums[p+1:], pending - 1)


def max_num12(line:str)->int:
    return max_num_recursive([int(x) for x in line.strip()], 12)

def compute_star1(file:str)->int:
    s = 0
    for line in load_file(file):
        s += max_num(line.strip())
    return s

def compute_star2(file:str)->int:
    s = 0
    for line in load_file(file):
        s += max_num12(line.strip())
    return s


if __name__ == "__main__":
    print(f"star1: {compute_star1('day3/example.txt')}")
    print(f"star1: {compute_star1('day3/data.txt')}")
    print(f"star2: {compute_star2('day3/example.txt')}")
    print(f"star2: {compute_star2('day3/data.txt')}")
