def solution():
    
    diamond_earrings_cost = 6000 * 2
    iphone_cost = 2000
    total_value = 20000
    scarves_value = total_value - diamond_earrings_cost - iphone_cost
    scarves_count = scarves_value / 1500
    result = scarves_count
    return result

print(solution())