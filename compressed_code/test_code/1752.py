def solution():
    
    lion_count = 100
    birth_rate = 5
    death_rate = 1
    for i in range(12): 
        lion_count = lion_count + birth_rate - death_rate
    result = lion_count
    return result

print(solution())