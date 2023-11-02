def solution():
    """Kekai's family is having a garage sale. Kekai sells 5 shirts and 5 pairs of pants. Each shirt sells for $1, and each pair of pants sells for $3. If Kekai gives his parents half of the money he earns from selling his clothes, how much money does Kekai have left?"""
    # Define the number of shirts and pants sold, and their respective prices
    num_shirts = 5
    shirt_price = 1
    num_pants = 5
    pant_price = 3

    # Calculate the total amount earned from selling clothes
    total_earned = num_shirts * shirt_price + num_pants * pant_price

    # Calculate the amount given to Kekai's parents
    parents_share = total_earned / 2

    # Calculate the amount of money Kekai has left
    kekai_share = total_earned - parents_share

    # Return the result
    result = kekai_share
    return result

print(solution())