def solution():
    # Calculate the number of pairs of slippers and boots Nancy has
    num_boots = 6
    num_slippers = num_boots + 9
    total_pair_shoes = num_boots + num_slippers

    # Calculate the number of pairs of heels Nancy has
    num_heels = 3 * (num_boots + num_slippers)

    # Calculate the total number of individual shoes Nancy has
    total_shoes = (2*num_boots) + (2*num_slippers) + (2*num_heels)

    result = total_shoes
    return result

print(solution())