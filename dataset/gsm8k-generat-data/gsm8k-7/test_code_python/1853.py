def solution():
    num_days = 7

    # Calculate the number of shirts needed for Monday and Sunday
    num_shirts = 1

    # Calculate the number of shirts needed for the other 5 days
    num_shirts += 2 * 5

    result = num_shirts
    return result

print(solution())