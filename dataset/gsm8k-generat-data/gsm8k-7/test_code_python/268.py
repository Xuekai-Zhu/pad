def solution():
    num_carnations = [9, 14, 13]
    num_bouquets = len(num_carnations)

    # Calculate the total number of carnations
    total_carnations = sum(num_carnations)

    # Calculate the average number of carnations
    average_carnations = total_carnations / num_bouquets
    result = average_carnations
    return result

print(solution())