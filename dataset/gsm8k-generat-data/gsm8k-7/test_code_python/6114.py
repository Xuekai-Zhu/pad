def solution():
    num_boots = 6
    num_slippers = num_boots + 9
    num_heels = 3 * (num_boots + num_slippers)

    # Calculate the total number of shoes
    total_shoes = (num_boots * 2) + (num_slippers * 2) + (num_heels * 2)

    result = total_shoes
    return result

print(solution())