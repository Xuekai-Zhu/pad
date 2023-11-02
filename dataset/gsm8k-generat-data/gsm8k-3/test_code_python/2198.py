def solution():
    """Jonas is trying to expand his wardrobe.  He has 20 pairs of socks, 5 pairs of shoes, 10 pairs of pants and 10 t-shirts.  How many pairs of socks does he need to buy to double the number of individual items in his wardrobe?"""
    # Define the initial number of individual items in Jonas's wardrobe
    initial_items = 20 + 5 + 10 + 10

    # Calculate the number of additional individual items needed to double the initial amount
    additional_items = initial_items

    while additional_items < initial_items * 2:
        additional_items += 2

    # Calculate the number of pairs of socks needed to obtain the additional individual items
    socks_needed = (additional_items - initial_items) // 2

    # Display the number of pairs of socks needed
    result = socks_needed
    return result

print(solution())