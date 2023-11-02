def solution():
    shoppers_prefer_to_avoid = 5/8
    shoppers_in_store = 480
    shoppers_at_checkout = shoppers_in_store * (1 - shoppers_prefer_to_avoid)
    result = shoppers_at_checkout
    return result

print(solution())