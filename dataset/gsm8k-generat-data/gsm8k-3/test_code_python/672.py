def solution():
    """Harris feeds his dog 1 large organic carrot over the course of 1 day.  There are 5 carrots in a 1 pound bag and each bag costs $2.00.  In one year, how much will Harris spend on carrots?"""
    # Define the number of carrots Harris feeds his dog per day
    carrots_per_day = 1

    # Define the number of bags of carrots Harris needs per year
    bags_per_year = 365 / 5 / carrots_per_day

    # Define the cost of each bag of carrots
    cost_per_bag = 2.00

    # Calculate the total cost of carrots per year
    total_cost = bags_per_year * cost_per_bag

    # Display the total cost of carrots per year
    result = total_cost
    return result

print(solution())