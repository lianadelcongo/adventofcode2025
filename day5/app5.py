

class Kitchen:
    def __init__(self, filename: str):
        self.ranges:list[tuple[int,int]] = []
        self.ingredients:list[int] = []
        with open(filename) as my_file:
            for line in my_file.readlines():
                clean_line = line.strip()
                if clean_line == "":
                    continue
                if "-" in clean_line:
                    (start, end) = clean_line.split("-")
                    self.ranges.append((int(start), int(end)))
                else:
                    self.ingredients.append(int(clean_line))    

    def is_fresh(self, ingredient:int)->bool:
        for r in self.ranges:
            if r[0]<= ingredient <= r[1]:
                return True
        return False

    def fresh_ingredients(self)->list[int]:
        fresh:list[int] = []
        for i in self.ingredients:
            if self.is_fresh(i):
                fresh.append(i)
        return fresh
    
    def can_be_merged(self, range1:tuple[int,int], range2:tuple[int,int])-> bool:
        (x1,x2) = range1
        (y1,y2) = range2
        
        if x1 <= y1 <= x2 or x1 <= y2 <= x2:
            return True
        
        if y1 <= x1 and y2 >= x2:
            return True
        return False 
    
    def merge(self, range1:tuple[int,int], range2:tuple[int,int])-> tuple[int,int]:
        (x1,x2) = range1
        (y1,y2) = range2
        
        return((min(x1,y1), max(x2,y2)))
    
    def merge_ranges(self)->None:
        current_ranges = [x for x in self.ranges]
        print(f"{current_ranges=}")
        new_ranges:list[tuple[int,int]] = []
        for i in range(0, len(current_ranges)):
            any_combined = False
            for j in range(i+1, len(current_ranges)):
                if self.can_be_merged(current_ranges[i], current_ranges[j]):
                    current_ranges[j] = self.merge(current_ranges[i], current_ranges[j])
                    any_combined = True
                    break
            if not any_combined:
                new_ranges.append(current_ranges[i])
        self.ranges = new_ranges                    
                
    def get_all_fresh(self)->int:
        f = 0
        for range in self.ranges:
            f += (1+range[1]-range[0])
        return f

def compute_star1(file:str)->int:
    k = Kitchen(file)
    return len(k.fresh_ingredients())

def compute_star2(file:str)->int:
    k = Kitchen(file)
    k.merge_ranges()
    return k.get_all_fresh()


if __name__ == "__main__":
    print(f"star1 example: {compute_star1('day5/example.txt')}")
    print(f"star1 data: {compute_star1('day5/data.txt')}")
    print(f"star2 example: {compute_star2('day5/example.txt')}")
    print(f"star2 data: {compute_star2('day5/data.txt')}")
