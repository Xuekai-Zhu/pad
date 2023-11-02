def solution():
    """The bagels cost $2.25 each, or a dozen for $24. How much is saved, per bagel, in cents, by buying a dozen at a time?"""
    individual_cost = 2.25
    dozen_cost = 24
    num_bagels_in_dozen = 12
    cost_per_dozen = dozen_cost / num_bagels_in_dozen
    savings_per_bagel = (individual_cost - cost_per_dozen) * 100
    result = savings_per_bagel
    return result

print(solution())