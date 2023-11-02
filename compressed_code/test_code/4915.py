def solution():
    
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