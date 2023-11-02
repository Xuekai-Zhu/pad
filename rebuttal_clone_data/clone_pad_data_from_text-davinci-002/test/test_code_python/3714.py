def solution():
    money = 15
    artichoke_cost = 1.25
    ounces = 5
    needed_artichokes = 3
    ounces_per_artichoke = ounces / needed_artichokes
    artichokes_purchasable = money / artichoke_cost
    result = ounces_per_artichoke * artichokes_purchasable
    return result

print(solution())