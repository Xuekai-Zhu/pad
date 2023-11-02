def solution():
    # Calculate how many artichokes Hakeem can buy with his budget
    budget = 15
    artichoke_cost = 1.25
    num_artichokes = budget / artichoke_cost

    # Calculate how many ounces of dip he can make
    num_ounces = (num_artichokes / 3) * 5
    result = num_ounces
    return result

print(solution())