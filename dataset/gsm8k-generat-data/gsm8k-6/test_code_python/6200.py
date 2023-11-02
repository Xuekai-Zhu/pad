def solution():
    # Calculate the number of houses built in the first half of the year
    first_half_houses = (3/5) * 2000

    # Calculate the total number of houses built up to October
    total_houses = first_half_houses + 300

    # Calculate the number of houses remaining to be built
    remaining_houses = 2000 - total_houses
    result = remaining_houses
    return result

print(solution())