def solution():
    """Jonas is trying to expand his wardrobe. He has 20 pairs of socks, 5 pairs of shoes, 10 pairs of pants and 10 t-shirts. How many pairs of socks does he need to buy to double the number of individual items in his wardrobe?"""
    num_items = 20 + 5 + 10 + 10
    desired_num_items = num_items * 2
    num_socks_needed = desired_num_items - num_items
    result = num_socks_needed
    return result

print(solution())