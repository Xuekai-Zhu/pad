def solution():
    """John and his two brothers decide to split the cost of an apartment. It is 40% more expensive than John's old apartment which costs $1200 per month. How much does John save per year by splitting the apartment compared to living alone?"""
    # Define the cost of John's old apartment and the increase in cost of the new apartment
    old_cost = 1200
    increase_percent = 40

    # Calculate the new cost of the apartment
    new_cost = old_cost * (1 + increase_percent/100)

    # Calculate John's share of the new rent, assuming he splits it with his two brothers
    john_share = new_cost/3

    # Calculate how much John saves per year by splitting the rent
    annual_savings = (old_cost - john_share) * 12

    # Return the result
    result = annual_savings
    return result

print(solution())