def solution():
    # Calculate the total miles Tom bikes in the first 183 days
    first_half_miles = 30 * 183

    # Calculate the total miles Tom bikes in the second half of the year
    second_half_miles = 35 * (365 - 183)

    # Calculate the total miles Tom bikes in the entire year
    total_miles = first_half_miles + second_half_miles
    result = total_miles
    return result

print(solution())