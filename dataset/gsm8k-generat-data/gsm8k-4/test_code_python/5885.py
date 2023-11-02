def solution():
    """As Dan is learning to screen-print t-shirts to sell at the craft fair, he makes t-shirts, over the first hour, at the rate of one every 12 minutes.
    Then, in the second hour, he makes one at the rate of every 6 minutes. How many t-shirts does he make over the course of those two hours?"""
    # Define the rates of t-shirt production in t-shirts per minute
    rate_1 = 1/12  # t-shirts per minute in the first hour
    rate_2 = 1/6   # t-shirts per minute in the second hour

    # Calculate the total number of t-shirts produced in the first hour
    tshirts_hour_1 = rate_1 * 60  # t-shirts per hour in the first hour

    # Calculate the total number of t-shirts produced in the second hour
    tshirts_hour_2 = rate_2 * 60  # t-shirts per hour in the second hour

    # Calculate the total number of t-shirts produced in two hours
    total_tshirts = tshirts_hour_1 + tshirts_hour_2

    result = round(total_tshirts)
    return result

print(solution())