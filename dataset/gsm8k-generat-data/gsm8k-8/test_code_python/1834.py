def solution():
    # Calculate the cost of lodging for the first 3 nights
    hostel_cost = 15 * 3

    # Calculate the cost of lodging for the 4th and 5th nights, split between Jimmy and his 2 friends
    cabin_cost = 45 / 3 * 2

    # Calculate the total lodging cost
    total_cost = hostel_cost + cabin_cost
    
    result = total_cost
    return result

print(solution())