def solution():
    num_socks = 20
    num_shoes = 5
    num_pants = 10
    num_shirts = 10

    # Calculate the current total number of items in his wardrobe
    total_items = num_socks + num_shoes + num_pants + num_shirts

    # Calculate the desired total number of items in his wardrobe after buying more socks
    desired_items = total_items * 2

    # Calculate the number of socks needed to reach the desired total number of items
    num_socks_needed = desired_items - (num_shoes + num_pants + num_shirts + num_socks)

    result = num_socks_needed
    return result

print(solution())