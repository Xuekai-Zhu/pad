def solution():
    
    num_eggs = 3 * 12
    num_people = 3
    eggs_per_omelet = 4
    total_omelets = num_eggs // eggs_per_omelet
    omelets_per_person = total_omelets // num_people
    result = omelets_per_person
    return result

print(solution())