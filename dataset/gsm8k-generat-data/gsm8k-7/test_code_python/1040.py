def solution():
    num_goats = 66
    num_chickens = 2*num_goats
    num_ducks = (num_goats + num_chickens)/2
    num_pigs = num_ducks/3

    # Calculate the difference between the number of goats and pigs
    diff = num_goats - num_pigs
    result = diff
    return result

print(solution())