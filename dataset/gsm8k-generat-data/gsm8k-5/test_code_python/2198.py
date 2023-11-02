def solution():
    current_items = 20 + 5 + 10 + 10  # Jonas currently has 20 pairs of socks, 5 pairs of shoes, 10 pairs of pants, and 10 t-shirts
    desired_items = current_items * 2  # Jonas wants to double the number of individual items in his wardrobe
    socks_needed = (desired_items - current_items) / 2  # Jonas only needs to buy pairs of socks to reach his goal

    result = socks_needed
    return result

print(solution())