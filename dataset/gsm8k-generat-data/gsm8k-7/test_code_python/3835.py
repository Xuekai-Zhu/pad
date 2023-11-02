def solution():
    num_starting_mice = 8
    num_pups_per_mouse = 6
    num_days_to_grow_up = 30
    num_pups_per_adult_mouse = 6
    num_pups_eaten_per_mouse = 2

    # Calculate the total number of mice after the first generation of pups
    num_first_gen_mice = num_starting_mice * (1 + num_pups_per_mouse)

    # Calculate the total number of mice after the second generation of pups
    num_second_gen_mice = num_first_gen_mice * (1 + num_pups_per_adult_mouse)

    # Calculate the total number of mice that are eaten by their parents
    num_mice_eaten = num_first_gen_mice * num_pups_eaten_per_mouse + num_second_gen_mice * num_pups_eaten_per_mouse

    # Calculate the total number of mice left
    num_mice_left = num_first_gen_mice + num_second_gen_mice - num_mice_eaten
    result = num_mice_left
    return result

print(solution())