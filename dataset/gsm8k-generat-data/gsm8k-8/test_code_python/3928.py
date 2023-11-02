def solution():
    # Convert 3 hours to minutes
    time = 3 * 60

    # Calculate the number of houses that can be painted in that time
    num_houses = time // 20

    result = num_houses
    return result

print(solution())