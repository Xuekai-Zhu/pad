def solution():
    """In order to train for his fights Rocky would run 4 miles on day one of training. Rocky would double the miles for day 2, and triple the miles from day 2 for day 3. How many miles did Rocky run in the first three days of training?"""
    # Define the number of miles run on day 1
    day1_miles = 4

    # Calculate the number of miles run on day 2
    day2_miles = day1_miles * 2

    # Calculate the number of miles run on day 3
    day3_miles = day2_miles * 3

    # Calculate the total number of miles run in the first three days
    total_miles = day1_miles + day2_miles + day3_miles

    # return the result
    result = total_miles
    return result

print(solution())