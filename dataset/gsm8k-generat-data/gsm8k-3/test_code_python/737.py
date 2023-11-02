def solution():
    """Michael has 4 packs of crayons and wants to buy 2 more. One pack of crayons costs $2.5. How much are all the packs of crayons Michael will have after the purchase worth?"""
    # Define the number of packs of crayons Michael has and wants to buy
    initial_packs = 4
    additional_packs = 2

    # Define the cost per pack of crayons
    cost_per_pack = 2.5

    # Calculate the total number of packs of crayons Michael will have
    total_packs = initial_packs + additional_packs

    # Calculate the total worth of all the packs of crayons
    total_worth = total_packs * cost_per_pack

    # Display the total worth
    result = total_worth
    return result

print(solution())