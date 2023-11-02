def solution():
    # Prices of services at each salon
    gustran_haircut = 45
    gustran_facial = 22
    gustran_nails = 30

    barbara_haircut = 30
    barbara_facial = 28
    barbara_nails = 40

    fancy_haircut = 34
    fancy_facial = 30
    fancy_nails = 20

    # Calculate the total price of services at each salon
    gustran_total = gustran_haircut + gustran_facial + gustran_nails
    barbara_total = barbara_haircut + barbara_facial + barbara_nails
    fancy_total = fancy_haircut + fancy_facial + fancy_nails

    # Find the minimum total price among the three salons
    cheapest_price = min(gustran_total, barbara_total, fancy_total)
    result = cheapest_price
    return result

print(solution())