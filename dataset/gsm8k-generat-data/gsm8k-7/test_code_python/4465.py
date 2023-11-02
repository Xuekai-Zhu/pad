def solution():
    num_eggs_per_nest1 = 5
    num_eggs_per_nest2 = 5
    num_eggs_per_nest3 = 3
    num_eggs_per_nest4 = 4

    # Calculate the total number of eggs in the first two nests
    total_eggs_nests1_2 = (num_eggs_per_nest1 + num_eggs_per_nest2) * 2

    # Calculate the total number of eggs in the third nest
    total_eggs_nest3 = num_eggs_per_nest3

    # Calculate the total number of eggs in the fourth nest
    total_eggs_nest4 = num_eggs_per_nest4

    # Calculate the total number of eggs found
    total_eggs = total_eggs_nests1_2 + total_eggs_nest3 + total_eggs_nest4
    result = total_eggs
    return result

print(solution())