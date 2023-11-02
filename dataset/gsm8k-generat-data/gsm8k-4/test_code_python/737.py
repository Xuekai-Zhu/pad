def solution():
    """Michael has 4 packs of crayons and wants to buy 2 more. One pack of crayons costs $2.5. How much are all the packs of crayons Michael will have after the purchase worth?"""
    # Define the price per pack of crayons and the number of packs Michael has and wants to buy
    CRAYON_PRICE = 2.5
    INITIAL_PACKS = 4
    NEW_PACKS = 2

    # Calculate the total number of packs after the purchase
    total_packs = INITIAL_PACKS + NEW_PACKS

    # Calculate the total cost of all the packs
    total_cost = total_packs * CRAYON_PRICE

    # Return the result
    result = total_cost
    return result

print(solution())