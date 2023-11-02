def solution():
    """
    A man is trying to maximize the amount of money he saves each month. In particular, he is trying to decide between two different apartments. 
    The first apartment costs $800 per month in rent and will cost an additional $260 per month in utilities. 
    The second apartment costs $900 per month and will cost an additional $200 per month in utilities.
    The first apartment is slightly further from the man's work, and the man would have to drive 31 miles per day to get to work.
    The second apartment is closer, and the man would only have to drive 21 miles to get to work.
    According to the IRS, each mile a person drives has an average cost of 58 cents. 
    If the man must drive to work 20 days each month, what is the difference between the total monthly costs of these two apartments after factoring in utility and driving-related costs (to the nearest whole dollar)?
    """
    first_rent = 800
    second_rent = 900
    first_utilities = 260
    second_utilities = 200
    first_driving_cost = 31 * 0.58 * 20
    second_driving_cost = 21 * 0.58 * 20
    first_total_cost = first_rent + first_utilities + first_driving_cost
    second_total_cost = second_rent + second_utilities + second_driving_cost
    result = round(second_total_cost - first_total_cost)
    return result

print(solution())