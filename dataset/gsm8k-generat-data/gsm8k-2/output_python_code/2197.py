def solution():
    """Jonas is trying to expand his wardrobe. He has 20 pairs of socks, 5 pairs of shoes, 10 pairs of pants and 10 t-shirts. How many pairs of socks does he need to buy to double the number of individual items in his wardrobe?"""
    initial_items = 20 + 5 + 10 + 10
    double_items = initial_items * 2
    current_socks = 20
    socks_needed = ((double_items - current_socks) / 2)
    result = socks_needed
    return result

print(solution())