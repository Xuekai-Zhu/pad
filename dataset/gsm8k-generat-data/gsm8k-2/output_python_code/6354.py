def solution():
    """Louis is making himself a velvet suit for a formal event. The velvet fabric he chose was $24 per yard. He bought a pattern for $15, and two spools of silver thread for $3 each. If he spent $141 for the pattern, thread, and fabric, how many yards of fabric did he buy?"""
    fabric_price = 24
    pattern_price = 15
    thread_price = 3
    total_price = 141
    thread_total_price = 2 * thread_price
    fabric_total_price = total_price - pattern_price - thread_total_price
    fabric_yards = fabric_total_price / fabric_price
    result = fabric_yards
    return result

print(solution())