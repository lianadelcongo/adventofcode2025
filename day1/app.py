
def load_file(filename: str)->list[str]:
    with open(filename) as my_file:
        return my_file.readlines()
    return []

def compute_rotations1(lines: list[str])->int:
    changes = 0
    position = 50
    
    for line in lines:
        if line[0] == "R":
            position = (position + int(line[1:]))%100
        else:
            position = (position - int(line[1:]))%100

        if  position == 0:
            changes += 1
        
    return changes

def compute_rotations2(lines: list[str])->int:
    changes = 0
    position = 50
    
    for line in lines:
        steps = int(line[1:])
        changes += (steps // 100)
        if line[0] == "R":
            new_position = (position + steps)%100
            if new_position < position:
                changes += 1
        else:
            new_position = (position - steps)%100
            if new_position > position:
                changes += 1
        position = new_position
        
    return changes


if __name__ == "__main__":
    print(f"star1: {compute_rotations1(load_file('day1/data.txt'))}")
    print(f"star2: {compute_rotations2(load_file('day1/data.txt'))}")
    
