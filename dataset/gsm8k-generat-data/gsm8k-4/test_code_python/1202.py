def solution():
    """A man is trying to maximize the amount of money he saves each month. In particular, he is trying to decide between two different apartments. The first apartment costs $800 per month in rent and will cost an additional $260 per month in utilities. The second apartment costs $900 per month and will cost an additional $200 per month in utilities. The first apartment is slightly further from the man's work, and the man would have to drive 31 miles per day to get to work. The second apartment is closer, and the man would only have to drive 21 miles to get to work. According to the IRS, each mile a person drives has an average cost of 58 cents. If the man must drive to work 20 days each month, what is the difference between the total monthly costs of these two apartments after factoring in utility and driving-related costs (to the nearest whole dollar)?"""
    # Define the costs of the two apartments and their associated utilities
    apt1_rent = 800
    apt1_util = 260
    apt2_rent = 900
    apt2_util = 200

    # Define the distances to work and the IRS mileage rate
    dist1 = 31
    dist2 = 21
    mileage_rate = 0.58

    # Calculate the monthly driving costs for each apartment
    drive1_cost = dist1 * mileage_rate * 20
    drive2_cost = dist2 * mileage_rate * 20

    # Calculate the total monthly costs for each apartment
    total1_cost = apt1_rent + apt1_util + drive1_cost
    total2_cost = apt2_rent + apt2_util + drive2_cost

    # Calculate the difference in costs between the two apartments
    diff_cost = round(total2_cost - total1_cost)

    return diff_cost

print(solution())