def solution():
    initial_weight = 80
    weight_of_first_statue = 10
    weight_of_second_statue = 18
    weight_of_third_and_fourth_statue = (initial_weight - weight_of_first_statue - weight_of_second_statue) / 2
    weight_of_discarded_marble = 22
    result = weight_of_third_and_fourth_statue
    return result

print(solution())