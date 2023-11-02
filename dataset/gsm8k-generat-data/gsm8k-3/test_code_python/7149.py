def solution():
    """Hillary always buys the Wednesday, Thursday and Friday editions of the local newspaper for $0.50 each.  On Sunday, she spends $2.00 to get that copy.  How much does she spend on the newspaper over 8 weeks?"""
    # Define the cost of each weekday edition
    WEEKDAY_PRICE = 0.5
    # Define the cost of the Sunday edition
    SUNDAY_PRICE = 2.0

    # Define the number of weeks
    num_weeks = 8

    # Calculate the cost of the weekday editions for 8 weeks
    weekday_cost = 3 * 3 * WEEKDAY_PRICE * num_weeks

    # Calculate the cost of the Sunday editions for 8 weeks
    sunday_cost = SUNDAY_PRICE * num_weeks

    # Calculate the total cost
    total_cost = weekday_cost + sunday_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())