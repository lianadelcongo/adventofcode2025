from app import compute_rotations1,compute_rotations2, load_file

def test_day1_star1():
    lines = load_file("day1/example.txt")
    assert(compute_rotations1(lines)==3)
    
def test_day1_star2():
    lines = load_file("day1/example.txt")
    assert(compute_rotations2(lines)==6)