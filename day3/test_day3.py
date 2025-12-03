from app3 import max_num, max_num12

def test_day3_max_num():
    assert(max_num("89111111")==91)
    assert(max_num("12345678")==78)
    assert(max_num("5111114")==54)
    assert(max_num("476544")==76)
    assert(max_num("4725448")==78)
    

def test_day3_max_num12():
    assert(max_num12("987654321111111")==987654321111)
    assert(max_num12("811111111111119")==811111111119)
    assert(max_num12("234234234234278")==434234234278)
    assert(max_num12("818181911112111")==888911112111)

