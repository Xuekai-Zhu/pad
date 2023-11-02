def solution():
    """Carrie and her mom go to the mall to buy new clothes for school. Carrie buys 4 shirts, 2 pairs of pants, and 2 jackets. Each shirt costs $8. Each pair of pants costs $18. Each jacket costs $60. If Carrie’s mom pays for half of the total cost of all the clothes, how much does Carrie pay for the clothes?"""
    # Define the cost of each type of clothing item
    SHIRT_PRICE = 8
    PANTS_PRICE = 18
    JACKET_PRICE = 60

    # Define the number of each type of clothing item purchased
    num_shirts = 4
    num_pants = 2
    num_jackets = 2

    # Calculate the total cost of the clothing items
    total_cost = (num_shirts * SHIRT_PRICE) + (num_pants * PANTS_PRICE) + (num_jackets * JACKET_PRICE)

    # Calculate the amount Carrie's mom pays
    mom_pays = total_cost / 2

    # Calculate the amount Carrie pays
    carrie_pays = total_cost - mom_pays

    # Display the amount Carrie pays
    result = carrie_pays
    return result

print(solution())