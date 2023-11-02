def solution():
    # Calculate the current number of individual items in Jonas' wardrobe
    current_items = 20 + 5*2 + 10 + 10  # 20 pairs of socks, 5 pairs of shoes (10 individual shoes), 10 pants, 10 t-shirts
    target_items = current_items * 2  # double the number of individual items

    # Calculate the number of pairs of socks Jonas needs to buy to reach his goal
    socks_needed = (target_items - current_items) // 2  # divide by 2 since one pair of socks counts as 2 individual items
    result = socks_needed
    return result

print(solution())