def solution():
    """Benjamin went to McDonald's to buy something for dinner. He bought a salad, a burger, and two packs of fries. He paid in total $15. How much did the burger cost, if one pack of fries was for $2 and the salad was three times that price?"""
    # Define the price of one pack of fries and the price of the salad
    FRIES_PRICE = 2
    SALAD_PRICE = 3 * FRIES_PRICE

    # Define the total cost and the number of packs of fries bought
    total_cost = 15
    num_fries = 2

    # Calculate the cost of the fries and the salad
    fries_cost = num_fries * FRIES_PRICE
    salad_cost = SALAD_PRICE

    # Calculate the cost of the burger
    burger_cost = total_cost - fries_cost - salad_cost

    # Display the cost of the burger
    result = burger_cost
    return result

print(solution())