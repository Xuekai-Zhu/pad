def solution():
    # Calculate the total number of brownies, cookies and donuts brought in by the students
    total_brownies = 30 * 12
    total_cookies = 20 * 24
    total_donuts = 15 * 12

    # Calculate the total number of items brought in by the students
    total_items = total_brownies + total_cookies + total_donuts

    # Calculate the total amount of money raised
    total_money_raised = total_items * 2

    result = total_money_raised
    return result

print(solution())