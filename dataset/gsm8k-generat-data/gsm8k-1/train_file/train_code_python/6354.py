def solution():
    """Louis is making himself a velvet suit for a formal event. The velvet fabric he chose was $24 per yard. He bought a pattern for $15, and two spools of silver thread for $3 each. If he spent $141 for the pattern, thread, and fabric, how many yards of fabric did he buy?"""
    fabric_price_per_yard = 24
    pattern_price = 15
    thread_price = 3  # per spool
    total_cost = 141
    # equation: fabric_price*yards + pattern_price + thread_price*2 = total_cost
    yards = (total_cost - pattern_price - thread_price * 2) / fabric_price_per_yard
    result = yards
    return result

print(solution())