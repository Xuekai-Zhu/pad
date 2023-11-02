def solution():
    
    uncles = 3
    aunts = 4
    cousins = (uncles + aunts) * 2
    siblings = 1 + 1  
    total_guests = uncles + aunts + cousins + siblings
    result = total_guests
    return result

print(solution())