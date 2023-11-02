def solution():
    """Benjamin went to McDonald's to buy something for dinner. He bought a salad, a burger, and two packs of fries. He paid in total $15. How much did the burger cost, if one pack of fries was for $2 and the salad was three times that price?"""
    fries_price = 2
    salad_price = 3 * fries_price
    total_price = 15
    burger_price = (total_price - (2 * fries_price) - salad_price) / 1
    result = burger_price
    return result

print(solution())