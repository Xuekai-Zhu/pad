def solution():
    """Maria found a store that sells handmade sweaters for $30 and a handmade scarf for $20. She wants to buy one for everyone in her family. She will buy 6 sweaters and 6 scarves. If she has saved $500, how much will be left in her savings after buying all these?"""
    num_sweaters = 6
    num_scarves = 6
    sweater_cost = 30
    scarf_cost = 20
    total_cost = (num_sweaters * sweater_cost) + (num_scarves * scarf_cost)
    remaining_savings = 500 - total_cost
    result = remaining_savings
    return result

print(solution())