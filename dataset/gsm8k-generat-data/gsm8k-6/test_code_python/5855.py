def solution():
    # Calculate the number of gummy worms remaining after each day
    total_gummy_worms = 4  # number of gummy worms remaining after 4 days
    for i in range(3, -1, -1):  # iterate over the previous 4 days backwards
        total_gummy_worms = (total_gummy_worms + 4) * 2  # calculate the number of gummy worms remaining after each day
        if i == 0:
            break  # stop iterating when we reach the first day

    # Calculate the number of gummy worms in the bag originally
    original_gummy_worms = total_gummy_worms + 4
    result = original_gummy_worms
    return result

print(solution())