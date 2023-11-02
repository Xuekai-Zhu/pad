def solution():
    """Karlee has 100 grapes and 3/5 as many strawberries as grapes. Giana and Ansley, two of her friends, come visiting, and she gives each of them 1/5 of each fruit. How many fruits is Karlee left with in total?"""
    grapes = 100
    strawberries = (3/5) * grapes
    total_fruits = grapes + strawberries
    each_friend_share = 1/5 * total_fruits

    karlee_remaining = total_fruits - (each_friend_share * 2)
    result = karlee_remaining
    return result

print(solution())