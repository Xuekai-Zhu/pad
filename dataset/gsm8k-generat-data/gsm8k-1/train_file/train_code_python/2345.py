def solution():
    """John decides to trade in his stereo system. His old system cost 250 dollars and he got 80% of the value for it. He then buys a system that costs $600 that he gets a 25% discount on. How much money came out of his pocket?"""
    old_system_cost = 250
    trade_in_value = old_system_cost * 0.8 
    new_system_cost = 600 * 0.75
    total_cost = new_system_cost - trade_in_value 
    result = total_cost
    return result

print(solution())