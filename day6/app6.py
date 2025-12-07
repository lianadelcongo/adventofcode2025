from functools import reduce


class Operation:
    def __init__(self, operator:str = '+'):
        self.operands:list[int] = []
        self.operator = operator
    
    def add_operand(self, op:int)->None:
        self.operands.append(op)
        
    def eval(self)->int:
        if self.operator == "+":
            return reduce(lambda x,y:x+y, self.operands)
        if self.operator == "*":
            return reduce(lambda x,y:x*y, self.operands)
        print(f"Operator {self.operator} not defined ")
        return -1

class Math:
    
    def __init__(self, filename: str):
        self.operations: list[Operation] = [] 
        with open(filename) as my_file:
            for line in my_file.readlines():
                clean_line = line.strip()
                if "+" in clean_line:
                    for i, op in enumerate(clean_line.split()):
                        self.operations[i].operator = op
                else:
                    for i, num in enumerate(clean_line.split()):
                        if len(self.operations) <= i:
                            self.operations.append(Operation())
                        self.operations[i].add_operand(int(num))
                            
    def eval_all(self)->list[int]:
        return [x.eval() for x in self.operations]            


class Math2:
    
    def __init__(self, filename: str):
        self.operations: list[Operation] = []
        self.lines: list[str] = []
        with open(filename) as my_file:
            for line in my_file.readlines():
                if "+" in line:
                    for op in line.split():
                        self.operations.append(Operation(op))
                else:
                    self.lines.append(line[:-1])
        self.compute_operands()
        
    
    def compute_operands(self)->None:
        operation = 0
        num = 0
        numbers:dict[int, dict[int, list[str]]] = {}
        for x in range(0,len(self.lines[0])):
            if operation not in numbers:
                numbers[operation] = {}
            all_spaces = True
            for y in range(0, len(self.lines)):
                if self.lines[y][x] != " ":
                    all_spaces = False
                    if num not in numbers[operation]:
                        numbers[operation][num] = [self.lines[y][x]]
                    else:       
                        numbers[operation][num].append(self.lines[y][x])
                    
            if all_spaces:
                operation += 1
                num = 0
            else:
                num += 1                
            all_spaces = True

        for i,op in enumerate(numbers):
            for num in numbers[op]:
                    self.operations[i].add_operand(int("".join(numbers[op][num])))
    
    def eval_all(self)->list[int]:
        return [x.eval() for x in self.operations]            

def compute_star1(file:str)->int:
    m = Math(file)
    return sum(m.eval_all())

def compute_star2(file:str)->int:
    m = Math2(file)
    return sum(m.eval_all())

if __name__ == "__main__":
    print(f"star1 example: {compute_star1('day6/example.txt')}")
    print(f"star1 data: {compute_star1('day6/data.txt')}")
    print(f"star2 example: {compute_star2('day6/example.txt')}")
    print(f"star2 data: {compute_star2('day6/data.txt')}")
