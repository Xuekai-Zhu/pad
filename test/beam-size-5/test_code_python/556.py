def solution():
    
    total_cages = 6
    hamsters = 3
    guinea_pigs = 3
    total_hamsters = hamsters * 10
    total_guinea_pigs = guinea_pigs * 5
    total_rodents = total_cages + total_hamsters + total_guinea_pigs
    result = total_rodents
    return result

print(solution())