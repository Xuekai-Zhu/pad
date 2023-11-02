def solution():
    
    initial_money = 5000
    motorcycle_cost = 2800
    concert_cost = (initial_money - motorcycle_cost) / 2
    final_money = concert_cost - (concert_cost / 4)
    result = final_money
    return result

print(solution())