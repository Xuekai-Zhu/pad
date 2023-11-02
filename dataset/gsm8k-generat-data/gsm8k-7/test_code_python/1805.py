def solution():
    num_female_doves = 20
    num_eggs_per_dove = 3
    hatch_rate = 3/4
    
    # Calculate the total number of eggs laid by all female doves
    total_eggs_laid = num_female_doves * num_eggs_per_dove
    
    # Calculate the total number of hatched eggs
    num_hatched_eggs = total_eggs_laid * hatch_rate
    
    # Calculate the total number of doves now
    total_doves = num_female_doves + (num_hatched_eggs * 2)
    result = total_doves
    return result

print(solution())