def solution():
    miles_day1 = 4  # Rocky runs 4 miles on day one
    miles_day2 = miles_day1 * 2  # Rocky runs double the miles from day one on day two
    miles_day3 = miles_day2 * 3  # Rocky runs triple the miles from day two on day three

    # Calculate the total miles Rocky ran in the first three days
    total_miles = miles_day1 + miles_day2 + miles_day3
    result = total_miles
    return result

print(solution())