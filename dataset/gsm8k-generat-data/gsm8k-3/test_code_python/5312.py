def solution():
    """Kekai's family is having a garage sale. Kekai sells 5 shirts and 5 pairs of pants. Each shirt sells for $1, and each pair of pants sells for $3. If Kekai gives his parents half of the money he earns from selling his clothes, how much money does Kekai have left?"""
    # Define the price of a shirt and a pair of pants
    SHIRT_PRICE = 1
    PANTS_PRICE = 3

    # Calculate the total amount of money earned from selling shirts
    shirt_total = SHIRT_PRICE * 5

    # Calculate the total amount of money earned from selling pants
    pants_total = PANTS_PRICE * 5

    # Calculate the total amount of money earned from selling clothes
    total = shirt_total + pants_total

    # Calculate the amount of money Kekai gives to his parents
    parents_share = total / 2

    # Calculate the amount of money Kekai has left
    remaining_money = total - parents_share

    # Display the amount of money Kekai has left
    result = remaining_money
    return result

print(solution())