
EMPTY = "."
ROLL = "@"

class Area:
    def __init__(self, filename: str):
        self.area:dict[int,dict[int, str]] = {}
        y = 0
        with open(filename) as my_file:
            for line in my_file.readlines():
                clean_line = line.strip()
                self.area[y] = {}
                for x in range(0, len(clean_line)):
                    self.area[y][x] = clean_line[x]
                y += 1

    def get_size(self)->tuple[int,int]:
        return (len(self.area[0]),len(self.area))

    def get_pos(self, x:int, y:int)->str:
        if  0 <= y < len(self.area) and 0 <= x < len(self.area[0]):
            return self.area[y][x]
        return EMPTY

    def remove(self, x:int, y:int)->None:
        self.area[y][x] = EMPTY
        
    def get_surroundings(self, x:int, y:int)->list[str]:
        offsets = ((-1,-1),(-1,0),(-1,+1),(+1,-1),(+1,0),(+1,+1),(0,-1),(0,+1))
        return [self.get_pos(x+off[0],y+off[1]) for off in offsets]
    
    def is_roll_and_accessible(self, x:int, y:int)->bool:
        if self.get_pos(x,y) != ROLL:
            return False
        return len(list(filter(lambda x:x==ROLL, self.get_surroundings(x,y))))<4


def compute_star1(file:str)->int:
    s = 0
    a = Area(file)
    (w,h) = a.get_size()
    for i in range(0,w):
        for j in range(0,h):
            s = s + 1 if a.is_roll_and_accessible(i,j) else s
    return s

def compute_star2(file:str)->int:
    total_removed = 0
    previous_loop_total = -1
    a = Area(file)
    (w,h) = a.get_size()
    
    while(total_removed != previous_loop_total):
        previous_loop_total = total_removed
        for i in range(0,w):
            for j in range(0,h):
                if a.is_roll_and_accessible(i,j):
                    total_removed += 1
                    a.remove(i,j)
    return total_removed



if __name__ == "__main__":
    print(f"star1 example: {compute_star1('day4/example.txt')}")
    print(f"star1 data: {compute_star1('day4/data.txt')}")
    print(f"star2 example: {compute_star2('day4/example.txt')}")
    print(f"star2 data: {compute_star2('day4/data.txt')}")
