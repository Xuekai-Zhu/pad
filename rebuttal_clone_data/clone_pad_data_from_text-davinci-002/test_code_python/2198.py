def solution():
    current_socks = 20
    current_shoes = 5
    current_pants = 10
    current_shirts = 10
    total_items = current_socks + current_shoes + current_pants + current_shirts
    double_total = total_items * 2
    socks_needed = double_total - total_items
    result = socks_needed
    return result

print(solution())