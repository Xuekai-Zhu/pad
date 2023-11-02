def solution():
    # Calculate the total cost of the car rental for 11 days
    if days <= 7:
        cost = 30 * days  # $30/day for rentals less than or equal to 7 days
    else:
        cost = 190 + 30 * (days - 7)  # $190 for the first week plus $30/day for additional days

    result = cost
    return result

print(solution())