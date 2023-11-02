def solution():
    # Calculate the current number of individual items in Jonas' wardrobe
    current_items = 20 + 5 + 10 + 10

    # Calculate the target number of individual items
    target_items = current_items * 2

    # Calculate the number of pairs of socks needed to achieve the target
    socks_needed = (target_items - current_items) / 2

    result = socks_needed
    return result

print(solution())