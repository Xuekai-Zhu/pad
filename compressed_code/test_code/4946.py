def solution():
    
    ladder1_rungs = 50
    ladder1_price = ladder1_rungs * 2
    ladder2_rungs = 60
    ladder2_price = ladder2_rungs * 2
    total_ladders = 10 + 20
    total_price = (ladder1_price * 10) + (ladder2_price * 20)
    result = total_price
    return result

print(solution())