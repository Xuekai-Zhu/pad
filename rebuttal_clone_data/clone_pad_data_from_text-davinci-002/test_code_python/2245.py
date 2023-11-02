def solution():
    
    initial_lions = 100
    birth_rate = 5
    death_rate = 1
    
    total_lions = initial_lions + (birth_rate - death_rate)
    result = total_lions
    
    return result

print(solution())