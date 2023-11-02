def solution():
    """Jay & Gloria were hosting a 4th of July party at their house. Jay invited 22 people and Gloria invited 36. They wanted to buy small American flags for everyone. The craft store was having a sale on small flags, 5 flags for $1.00. If they wanted all of their guests to have a flag and they also wanted 1 flag each, how much would they spend at the craft store?"""
    # Calculate the total number of guests
    total_guests = 22 + 36

    # Calculate the total number of flags needed
    total_flags = total_guests + 2

    # Calculate the total cost of the flags
    flags_per_dollar = 5
    cost_per_dollar = 1
    full_dollars = total_flags // flags_per_dollar
    partial_dollars = total_flags % flags_per_dollar
    total_cost = full_dollars * cost_per_dollar + (partial_dollars / flags_per_dollar)

    # return the result
    result = round(total_cost, 2)
    return result

print(solution())