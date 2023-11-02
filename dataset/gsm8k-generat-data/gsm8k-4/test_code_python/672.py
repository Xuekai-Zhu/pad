def solution():
    """Harris feeds his dog 1 large organic carrot over the course of 1 day. There are 5 carrots in a 1 pound bag and each bag costs $2.00. In one year, how much will Harris spend on carrots?"""
    # Define the number of carrots consumed in a day and in a year
    carrots_per_day = 1
    carrots_per_year = carrots_per_day * 365

    # Define the number of bags of carrots needed in a year
    bags_per_year = carrots_per_year / 5

    # Define the cost of one bag of carrots and the total cost of carrots in a year
    cost_per_bag = 2.00
    cost_per_year = bags_per_year * cost_per_bag

    # return the result
    result = cost_per_year
    return result

print(solution())