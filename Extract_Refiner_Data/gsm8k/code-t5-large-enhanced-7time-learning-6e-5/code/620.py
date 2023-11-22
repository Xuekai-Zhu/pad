def solution():
    
    baseball_price = 3
    basketball_price = 14
    baseball_count = 9
    basketball_count = 8
    total_baseball_cost = baseball_price * baseball_count
    total_basketball_cost = basketball_price * basketball_count
    difference = total_basketball_cost - total_baseball_cost
    result = difference
    return result

print(solution())