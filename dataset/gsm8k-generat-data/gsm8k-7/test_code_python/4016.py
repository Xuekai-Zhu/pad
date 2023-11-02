def solution():
    sheep = 7
    pigs = -3
    total_count = 60

    # Adjust the count for the double-counted sheep and the forgotten pigs
    adjusted_count = total_count - (sheep/2) + pigs

    # Calculate the actual count of animals
    actual_count = adjusted_count
    result = actual_count
    return result

print(solution())