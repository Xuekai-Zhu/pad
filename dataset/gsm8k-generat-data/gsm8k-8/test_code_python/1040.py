def solution():
    # Calculate the number of chickens
    num_chickens = 2 * 66

    # Calculate the total number of goats and chickens
    total_goats_chickens = 66 + num_chickens

    # Calculate the number of ducks
    num_ducks = (total_goats_chickens) / 2

    # Calculate the number of pigs
    num_pigs = num_ducks / 3

    # Calculate the difference between the number of goats and pigs
    diff_goats_pigs = 66 - num_pigs

    result = diff_goats_pigs
    return result

print(solution())