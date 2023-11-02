def solution():
    
    total_weight = 80
    weight_of_first_statue = 10
    weight_of_second_statue = 18
    weight_of_discarded_marble = 22
    weight_of_remaining_statues = total_weight - (weight_of_first_statue + weight_of_second_statue + weight_of_discarded_marble)
    weight_of_each_remaining_statue = weight_of_remaining_statues / 2
    result = weight_of_each_remaining_statue
    return result

print(solution())