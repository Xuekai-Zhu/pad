def solution():
    """Haily wants to go to the salon and do her nails, cut her hair and do a facial cleaning. She doesn't want to spend much, so she called 3 salons to get their prices: Gustran Salon, Barbara's Shop, and The Fancy Salon. At Gustran Salon, the haircut is $45, the facial cleaning is $22 and the nails are $30. At Barbara's shop, the nails are $40, the haircut is $30 and the facial cleaning is $28. And, at the Fancy Salon, the facial cleaning is $30, the haircut is $34 and the nails are $20. How much would Haily spend at the cheapest salon?"""
    # Define the prices of the services at each salon
    GUSTRAN_HAIR = 45
    GUSTRAN_FACE = 22
    GUSTRAN_NAILS = 30
    BARBARA_HAIR = 30
    BARBARA_FACE = 28
    BARBARA_NAILS = 40
    FANCY_HAIR = 34
    FANCY_FACE = 30
    FANCY_NAILS = 20

    # Determine the total cost at each salon
    total_gustran = GUSTRAN_HAIR + GUSTRAN_FACE + GUSTRAN_NAILS
    total_barbara = BARBARA_HAIR + BARBARA_FACE + BARBARA_NAILS
    total_fancy = FANCY_HAIR + FANCY_FACE + FANCY_NAILS

    # Determine the minimum total cost
    min_cost = min(total_gustran, total_barbara, total_fancy)

    # Display the minimum cost
    result = min_cost
    return result

print(solution())