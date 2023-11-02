def solution():
    budget = 15  # Hakeem has $15 to buy artichokes
    cost_per_artichoke = 1.25  # Each artichoke costs $1.25
    artichokes_bought = budget // cost_per_artichoke  # Hakeem can buy the maximum number of artichokes
    ounces_per_artichoke = 5 / 3  # 3 artichokes make 5 ounces of dip
    total_ounces = artichokes_bought * ounces_per_artichoke  # Calculate the total ounces Hakeem can make
    result = total_ounces
    return result

print(solution())