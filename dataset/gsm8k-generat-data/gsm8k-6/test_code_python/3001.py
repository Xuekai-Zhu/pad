def solution():
    # Calculate the total miles walked by the group and by Jamie and Sue individually
    total_miles_group = 3 * 6  # the group walks 3 miles for 6 days
    miles_Jamie = (2 * 6) + (3 * 6)  # Jamie walks 2 additional miles per day for 6 days, plus the 3 miles with the group
    miles_Sue = (1/2) * (2 * 6)  # Sue walks half the distance Jamie does on the additional 2 miles per day for 6 days
    total_miles = total_miles_group + miles_Jamie + miles_Sue  # total miles walked by everyone

    result = total_miles
    return result

print(solution())