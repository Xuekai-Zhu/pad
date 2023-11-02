def solution():
    """Miss Darlington has a basket of 20 blueberries. She picked 9 more baskets with the same amount of berries. How many blueberries did Miss Darlington have in all?"""
    baskets_picked = 9
    blueberries_per_basket = 20
    total_blueberries = (baskets_picked + 1) * blueberries_per_basket
    result = total_blueberries
    return result

print(solution())