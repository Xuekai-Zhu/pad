def solution():
    """Haily wants to go to the salon and do her nails, cut her hair and do a facial cleaning. She doesn't want to spend much, so she called 3 salons to get their prices: Gustran Salon, Barbara's Shop, and The Fancy Salon. At Gustran Salon, the haircut is $45, the facial cleaning is $22 and the nails are $30. At Barbara's shop, the nails are $40, the haircut is $30 and the facial cleaning is $28. And, at the Fancy Salon, the facial cleaning is $30, the haircut is $34 and the nails are $20. How much would Haily spend at the cheapest salon?"""
    gustran_total_price = 45 + 22 + 30
    barbara_total_price = 40 + 30 + 28
    fancy_total_price = 30 + 34 + 20

    cheapest_price = min(gustran_total_price, barbara_total_price, fancy_total_price)

    result = cheapest_price
    return result

print(solution())