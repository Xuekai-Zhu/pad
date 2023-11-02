def solution():
    
    oreos_ratio = 4
    cookies_ratio = 9
    total_items = 65
    total_ratio = oreos_ratio + cookies_ratio
    oreos_count = (oreos_ratio / total_ratio) * total_items
    cookies_count = (cookies_ratio / total_ratio) * total_items
    oreos_cost = oreos_count * 2
    cookies_cost = cookies_count * 3
    difference = cookies_cost - oreos_cost
    result = difference
    return result

print(solution())