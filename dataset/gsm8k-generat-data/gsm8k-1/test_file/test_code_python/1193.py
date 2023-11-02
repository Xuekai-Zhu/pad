def solution():
    """John buys 10 bottles of scotch for a total cost of $600. He also buys twice as many bottles of cognac that cost 50% more per bottle. How much does he spend on everything?"""
    scotch_count = 10
    scotch_cost = 600
    cognac_count = scotch_count * 2
    cognac_cost_per_bottle = scotch_cost * 1.5
    total_spent = scotch_cost + (cognac_count * cognac_cost_per_bottle)
    result = total_spent
    return result

print(solution())