def solution():
    # Calculate the amount of flour remaining in the bag after baking cookies on Tuesday
    remaining_flour = 500 - 240  # 240g used for baking cookies
    remaining_flour = remaining_flour / 2  # half of remaining flour spilled accidentally
    # Calculate the amount of flour Lucy needs to buy to have a full bag
    flour_to_buy = 500 - remaining_flour
    result = flour_to_buy
    return result

print(solution())