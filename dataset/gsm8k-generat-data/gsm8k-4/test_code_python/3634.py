def solution():
    """Haily wants to go to the salon and do her nails, cut her hair and do a facial cleaning. She doesn't want to spend much, so she called 3 salons to get their prices: Gustran Salon, Barbara's Shop, and The Fancy Salon. At Gustran Salon, the haircut is $45, the facial cleaning is $22 and the nails are $30. At Barbara's shop, the nails are $40, the haircut is $30 and the facial cleaning is $28. And, at the Fancy Salon, the facial cleaning is $30, the haircut is $34 and the nails are $20. How much would Haily spend at the cheapest salon?"""
    # Define the prices of the services at each salon
    gustran_haircut = 45
    gustran_facial = 22
    gustran_nails = 30

    barbara_haircut = 30
    barbara_facial = 28
    barbara_nails = 40

    fancy_haircut = 34
    fancy_facial = 30
    fancy_nails = 20

    # Calculate the total cost of services at each salon
    gustran_cost = gustran_haircut + gustran_facial + gustran_nails
    barbara_cost = barbara_haircut + barbara_facial + barbara_nails
    fancy_cost = fancy_haircut + fancy_facial + fancy_nails

    # Find the cheapest salon
    cheapest_cost = min(gustran_cost, barbara_cost, fancy_cost)

    result = cheapest_cost
    return result

print(solution())