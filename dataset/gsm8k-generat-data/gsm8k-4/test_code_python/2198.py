def solution():
    """Jonas is trying to expand his wardrobe. He has 20 pairs of socks, 5 pairs of shoes, 10 pairs of pants and 10 t-shirts. How many pairs of socks does he need to buy to double the number of individual items in his wardrobe?"""
    # Calculate the initial number of items in Jonas's wardrobe
    initial_items = 20 + 5 + 10 + 10

    # Double the number of items and subtract the initial number of items to get the additional number of items needed
    additional_items = 2 * initial_items - 20

    # Divide the additional number of items by 2 to get the number of pairs of socks needed to purchase
    socks_needed = additional_items / 2

    result = socks_needed
    return result

print(solution())