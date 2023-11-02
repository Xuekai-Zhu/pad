def solution():
    """John and his two brothers decide to split the cost of an apartment. It is 40% more expensive than John's old apartment which costs $1200 per month. How much does John save per year by splitting the apartment compared to living alone?"""
    old_apartment_cost = 1200
    new_apartment_cost = old_apartment_cost * 1.4
    total_cost = new_apartment_cost / 3
    john_savings = old_apartment_cost - (total_cost)
    annual_savings = john_savings * 12
    result = annual_savings
    return result

print(solution())