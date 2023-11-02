def solution():
    num_hens = 3
    eggs_per_day = 3
    num_days = 7
    eggs_taken_by_neighbor = 12
    eggs_dropped_on_the_way = 5

    # Calculate the total number of eggs laid by the hens during the 7 days
    total_eggs_laid = num_hens * eggs_per_day * num_days

    # Calculate the total number of eggs that Myrtle has after the neighbor takes some and she drops some
    total_eggs = total_eggs_laid - eggs_taken_by_neighbor - eggs_dropped_on_the_way
    result = total_eggs
    return result

print(solution())