def solution():
    # Prices at Gustran Salon
    gustran_haircut = 45
    gustran_facial = 22
    gustran_nails = 30

    # Prices at Barbara's Shop
    barbara_haircut = 30
    barbara_facial = 28
    barbara_nails = 40

    # Prices at The Fancy Salon
    fancy_haircut = 34
    fancy_facial = 30
    fancy_nails = 20

    # Calculate the total cost at each salon
    gustran_cost = gustran_haircut + gustran_facial + gustran_nails
    barbara_cost = barbara_haircut + barbara_facial + barbara_nails
    fancy_cost = fancy_haircut + fancy_facial + fancy_nails

    # Find the cheapest option
    cheapest = min(gustran_cost, barbara_cost, fancy_cost)

    result = cheapest
    return result

print(solution())