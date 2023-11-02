def solution():
    total_cakes = 60
    cakes_already_made = total_cakes / 2

    # Calculate the number of cakes left to make after first batch
    cakes_left_first_batch = total_cakes - cakes_already_made

    # Calculate the number of cakes baked on the first day
    cakes_baked_first_day = cakes_left_first_batch / 2

    # Calculate the number of cakes left to make after second batch
    cakes_left_second_batch = cakes_left_first_batch - cakes_baked_first_day

    # Calculate the number of cakes baked on the second day
    cakes_baked_second_day = cakes_left_second_batch / 3

    # Calculate the total number of cakes left to make
    total_cakes_left = cakes_left_second_batch - cakes_baked_second_day

    result = total_cakes_left
    return result

print(solution())