def solution():
    
    initial_items = 20 + 5 + 10 + 10
    double_items = initial_items * 2
    current_socks = 20
    socks_needed = ((double_items - current_socks) / 2)
    result = socks_needed
    return result

print(solution())