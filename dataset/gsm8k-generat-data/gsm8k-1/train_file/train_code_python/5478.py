def solution():
    """A guy goes to the tool shop and buys 5 sets of drill bits. Each set cost 6 dollars. He then pays 10% tax on the order. What was the total amount he paid?"""
    sets_of_drill_bits = 5
    cost_per_set = 6
    pre_tax_total = sets_of_drill_bits * cost_per_set
    tax_rate = 0.10
    tax_amount = pre_tax_total * tax_rate
    total_cost = pre_tax_total + tax_amount
    result = total_cost
    return result

print(solution())