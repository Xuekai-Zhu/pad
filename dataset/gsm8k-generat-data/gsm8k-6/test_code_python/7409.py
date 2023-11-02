def solution():
    # Calculate the total number of squares of toilet paper used per day
    squares_per_day = 3 * 5  # Bill goes to the bathroom three times a day and uses 5 squares of toilet paper each time

    # Calculate the total number of squares of toilet paper available to Bill
    total_squares = 1000 * 300  # each roll has 300 squares of toilet paper

    # Calculate the number of days Bill's toilet paper supply will last
    days = total_squares // squares_per_day
    result = days
    return result

print(solution())