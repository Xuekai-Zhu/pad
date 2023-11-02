def solution():
    
    ants_first_anthill = 100
    ants_second_anthill = ants_first_anthill - (ants_first_anthill * 0.20)
    ants_third_anthill = ants_second_anthill - (ants_second_anthill * 0.20)
    result = ants_third_anthill
    return result

print(solution())