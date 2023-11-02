def solution():
    
    starting_weight = 80
    first_statue = 10
    second_statue = 18
    discarded_marble = 22
    remaining_weight = starting_weight - first_statue - second_statue - discarded_marble
    remaining_statues_weight = remaining_weight / 2
    result = remaining_statues_weight
    return result

print(solution())