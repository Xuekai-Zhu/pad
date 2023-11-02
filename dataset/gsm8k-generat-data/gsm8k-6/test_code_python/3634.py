def solution():
    # Calculate the total cost at each salon
    Gustan_Salon = 45 + 22 + 30
    Barbara_Shop = 40 + 30 + 28
    Fancy_Salon = 30 + 34 + 20

    # Find the cheapest salon among the three
    cheapest_salon = min(Gustan_Salon, Barbara_Shop, Fancy_Salon)
    result = cheapest_salon
    return result

print(solution())