def solution():
    """Miss Darlington has a basket of 20 blueberries. She picked 9 more baskets with the same amount of berries. How many blueberries did Miss Darlington have in all?"""
    # Define the number of blueberries in one basket
    BLUEBERRIES_PER_BASKET = 20

    # Define the number of baskets picked
    num_baskets = 9

    # Calculate the total number of blueberries
    total_blueberries = (num_baskets + 1) * BLUEBERRIES_PER_BASKET

    # Display the total number of blueberries
    result = total_blueberries
    return result

print(solution())