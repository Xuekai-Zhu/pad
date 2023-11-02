def solution():
    # Calculate the total miles Rocky ran in the first three days of training
    day_one = 4  # Rocky ran 4 miles on day one
    day_two = 2 * day_one  # Rocky doubled his miles from day one
    day_three = 3 * day_two  # Rocky tripled his miles from day two
    total_miles = day_one + day_two + day_three
    result = total_miles
    return result

print(solution())