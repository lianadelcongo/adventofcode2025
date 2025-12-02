from day2.app2 import isRepeatedTwiceNumber, isRepeatedNumber, checkRange

def test_day2_isRepeatedTwiceNumber():
    assert(not isRepeatedTwiceNumber(1))
    assert(isRepeatedTwiceNumber(11))
    assert(not isRepeatedTwiceNumber(111))
    assert(isRepeatedTwiceNumber(1111))
    assert(isRepeatedTwiceNumber(111111))
    assert(not isRepeatedTwiceNumber(202))
    assert(isRepeatedTwiceNumber(34553455))

def test_day2_checkRange():
    assert(checkRange(11,22, isRepeatedTwiceNumber)==33)
    assert(checkRange(95,115,isRepeatedTwiceNumber)==99)
    assert(checkRange(38593856,38593862,isRepeatedTwiceNumber)==38593859)
    assert(checkRange(565653,565659,isRepeatedTwiceNumber)==0)
    
def test_day2_isRepeatedNumber():
    assert(not isRepeatedNumber(1))
    assert(isRepeatedNumber(11))
    assert(isRepeatedNumber(111))
    assert(isRepeatedNumber(1111))
    assert(isRepeatedNumber(121212))
    assert(isRepeatedNumber(111111))
    assert(not isRepeatedNumber(1111112))
    assert(isRepeatedNumber(345345345))
    assert(not isRepeatedNumber(3453453452))
    assert(not isRepeatedNumber(202))
    assert(isRepeatedNumber(34553455))

def test_day2_checkRange2():
    assert(checkRange(11,22, isRepeatedNumber)==33)
    assert(checkRange(95,115,isRepeatedNumber)==210)
    assert(checkRange(38593856,38593862,isRepeatedNumber)==38593859)
    assert(checkRange(565653,565659,isRepeatedNumber)==565656)
