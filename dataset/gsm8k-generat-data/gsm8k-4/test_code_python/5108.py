def solution():
    """Benjamin went to McDonald's to buy something for dinner. He bought a salad, a burger, and two packs of fries. He paid in total $15. How much did the burger cost, if one pack of fries was for $2 and the salad was three times that price?"""
    # Define the price of one pack of fries and the price of the salad
    fries_price = 2
    salad_price = 3 * fries_price

    # Calculate the total price of the meal
    total_price = fries_price * 2 + salad_price + burger_price

    # Calculate the price of the burger
    burger_price = (total_price - 2*fries_price - salad_price) / 2

    result = burger_price
    return result

print(solution())