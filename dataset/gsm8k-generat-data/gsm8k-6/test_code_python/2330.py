def solution():
    # Calculate the area of the mural in square feet
    area = 20 * 15

    # Calculate the time it takes to paint the mural in hours
    time = (20 * area) / 60

    # Calculate the total cost of painting the mural
    cost = time * 150

    result = cost
    return result

print(solution())