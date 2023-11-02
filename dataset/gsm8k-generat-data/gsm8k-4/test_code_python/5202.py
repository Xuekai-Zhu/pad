def solution():
    """The snack machine at Richmond High School sells candy bars for $2 each and chips for $.50 each.
    How much money, in dollars, will 5 students need in total if each of them gets 1 candy bar and 2 bags of chips?"""
    # Define the prices of candy bars and chips
    candy_bar_price = 2
    chip_price = 0.5

    # Calculate the total cost for each student
    cost_per_student = candy_bar_price + (2 * chip_price)

    # Calculate the total cost for 5 students
    total_cost = cost_per_student * 5

    # Return the result
    result = total_cost
    return result

print(solution())