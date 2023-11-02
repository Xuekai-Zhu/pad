def solution():
    # Calculate the total number of brownies brought in by the students
    total_brownies = 30 * 12

    # Calculate the total number of cookies brought in by the students
    total_cookies = 20 * 24

    # Calculate the total number of donuts brought in by the students
    total_donuts = 15 * 12

    # Calculate the total number of items brought in by the students
    total_items = total_brownies + total_cookies + total_donuts

    # Calculate the amount of money raised by selling all items at $2 each
    total_money = total_items * 2.0
    result = total_money
    return result

print(solution())