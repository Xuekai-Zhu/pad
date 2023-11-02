def solution():
    # Calculate the total time it takes to fix all the shirts and pants
    shirt_time = 1.5 * 10  # time to fix all shirts
    pant_time = 1.5 * 2 * 12  # time to fix all pants (twice as long as shirts)
    total_time = shirt_time + pant_time  # total time to fix all shirts and pants

    # Calculate the total cost for the seamstress
    cost = total_time * 30  # $30 per hour
    result = cost
    return result

print(solution())