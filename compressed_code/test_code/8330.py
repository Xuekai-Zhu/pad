def solution():
    
    initial_chickens = 400
    death_percent = 40
    death_count = initial_chickens * (death_percent / 100)
    bought_count = death_count * 10
    total_chickens = initial_chickens - death_count + bought_count
    result = total_chickens
    return result

print(solution())