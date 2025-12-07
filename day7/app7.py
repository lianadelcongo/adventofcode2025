from collections import defaultdict

EMPTY = "."
SPLIT = "^"
START = "S"
BEAM = "|"
OUT  = "O"

class Area:
    def __init__(self, filename: str):
        self.area:dict[int,dict[int, str]] = {}
        self.splitters:set[tuple[int, int]] = set()
        self.splitted = 0
        y = 0
        with open(filename) as my_file:
            for line in my_file.readlines():
                clean_line = line.strip()
                self.area[y] = {}
                for x in range(0, len(clean_line)):
                    self.area[y][x] = clean_line[x]
                    if self.area[y][x] == START:
                        self.pending_moves = [(x,y)]
                    if self.area[y][x] == SPLIT:
                        self.splitters.add((x,y))
                y += 1

    def get_size(self)->tuple[int,int]:
        return (len(self.area[0]),len(self.area))

    def get_pos(self, x:int, y:int)->str:
        if  0 <= y < len(self.area) and 0 <= x < len(self.area[0]):
            return self.area[y][x]
        return OUT

    def remove(self, x:int, y:int)->None:
        self.area[y][x] = EMPTY

    def visit(self, x:int, y:int)->bool:
        if self.get_pos(x,y) == EMPTY:
            self.area[y][x] = BEAM
            return True
        return False
        
    def has_pending_iterations(self)->bool:
        return len(self.pending_moves) > 0
        
    def iterate(self)->None:
        new_moves:list[tuple[int, int]] = []
        for (mx, my) in self.pending_moves:
            if self.get_pos(mx, my + 1) == EMPTY:
                self.visit(mx, my + 1)
                new_moves.append((mx, my + 1))
            if self.get_pos(mx, my + 1) == SPLIT:
                self.splitted += 1
                if self.visit(mx - 1, my + 1):
                    new_moves.append((mx - 1, my + 1))
                if self.visit(mx + 1, my + 1):
                    new_moves.append((mx + 1, my + 1))
        self.pending_moves = new_moves
    
    def find_num_paths(self)->int:
        paths_finished = 0
        paths:dict[tuple[int, int], int] = {(x,y):1 for (x,y) in self.pending_moves}
        while len(paths) > 0:
            new_paths:defaultdict[tuple[int, int], int] = defaultdict(lambda: 0)
            for (mx, my) in paths:
                number = paths[(mx, my)]
                if self.get_pos(mx, my + 1) == EMPTY:
                    new_paths[(mx, my + 1)] = new_paths[(mx, my + 1)] + number
                if self.get_pos(mx, my + 1) == SPLIT:
                    new_paths[(mx + 1, my + 1)] = new_paths[(mx + 1, my + 1)] + number 
                    new_paths[(mx - 1, my + 1)] = new_paths[(mx - 1, my + 1)] + number
                if self.get_pos(mx, my + 1) == OUT:
                    paths_finished += number
            paths = new_paths
        return paths_finished
            
def compute_star1(file:str)->int:
    a = Area(file)
    while a.has_pending_iterations():
        a.iterate()
    return a.splitted

def compute_star2(file:str)->int:
    a = Area(file)
    return a.find_num_paths()
    
if __name__ == "__main__":
    print(f"star1 example: {compute_star1('day7/example.txt')}")
    print(f"star1 data: {compute_star1('day7/data.txt')}")
    print(f"star2 example: {compute_star2('day7/example.txt')}")
    print(f"star2 data: {compute_star2('day7/data.txt')}")
