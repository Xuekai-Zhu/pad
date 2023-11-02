def solution():
    bonny_shoes = 13
    
    # Let b be the number of shoes that Becky owns
    # Then 2b - 5 = bonny_shoes
    # And b = (bonny_shoes + 5)/2
    b = (bonny_shoes + 5) / 2
    
    # Bobby has 3 times as many shoes as Becky
    # So Bobby has 3b shoes
    bobby_shoes = 3 * b
    
    result = bobby_shoes
    return result

print(solution())