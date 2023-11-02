def solution():
    # Calculate the total days of the vacation
    total_days = 7

    # Calculate the total number of different shirts needed for the 5 days
    different_shirts = 2 * 5

    # Add 1 shirt for departure and 1 shirt for return
    total_shirts = different_shirts + 2
    result = total_shirts
    return result

print(solution())