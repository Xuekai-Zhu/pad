def solution():
    total_blocks_used = 1
    starting_weight = 80
    discarded_weight = 22
    weight_of_first_statue = 10
    weight_of_second_statue = 18

    # Calculate the weight of the marble of the remaining two statues and add it to the weight of the first two statues
    weight_of_first_two_statues = weight_of_first_statue + weight_of_second_statue
    weight_of_remaining_marble = starting_weight - weight_of_first_two_statues - discarded_weight
    weight_of_each_remaining_statue = weight_of_remaining_marble / 2
    result = weight_of_each_remaining_statue
    return result

print(solution())