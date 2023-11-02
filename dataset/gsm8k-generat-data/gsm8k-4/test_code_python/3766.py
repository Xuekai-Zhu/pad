def solution():
    """Miss Darlington has a basket of 20 blueberries. She picked 9 more baskets with the same amount of berries. How many blueberries did Miss Darlington have in all?"""
    # Define the number of blueberries in each basket
    blueberries_per_basket = 20

    # Define the number of baskets picked
    baskets_picked = 9

    # Calculate the total number of blueberries
    total_blueberries = blueberries_per_basket * (baskets_picked + 1)

    # Return the result
    result = total_blueberries
    return result

print(solution())