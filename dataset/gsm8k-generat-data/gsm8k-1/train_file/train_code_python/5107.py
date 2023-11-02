def solution():
    """Benjamin went to McDonald's to buy something for dinner. He bought a salad, a burger, and two packs of fries. He paid in total $15. How much did the burger cost, if one pack of fries was for $2 and the salad was three times that price?"""
    total_cost = 15
    fries_cost = 2 * 2
    salad_cost = 3 * fries_cost
    burger_cost = total_cost - fries_cost - salad_cost
    result = burger_cost
    return result

print(solution())