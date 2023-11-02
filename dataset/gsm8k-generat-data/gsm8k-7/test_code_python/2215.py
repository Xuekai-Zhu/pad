def solution():
    num_men = 80
    fraction_tripped = 1/4
    fraction_remaining = 1 - fraction_tripped

    # Calculate the number of men who couldn't finish due to tripping
    num_tripped = num_men * fraction_tripped

    # Calculate the number of men who remained in the race
    num_remaining = num_men - num_tripped

    # Calculate the number of dehydrated men
    num_dehydrated = num_remaining * (2/3)

    # Calculate the number of dehydrated men who couldn't finish
    num_unfinished = num_dehydrated * (1/5)

    # Calculate the number of men who finished the race
    num_finished = num_remaining - num_unfinished
    result = num_finished
    return result

print(solution())