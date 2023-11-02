def solution():
    """Kekai's family is having a garage sale. Kekai sells 5 shirts and 5 pairs of pants. Each shirt sells for $1, and each pair of pants sells for $3. If Kekai gives his parents half of the money he earns from selling his clothes, how much money does Kekai have left?"""
    num_shirts = 5
    shirt_price = 1
    num_pants = 5
    pant_price = 3
    total_earnings = (num_shirts * shirt_price) + (num_pants * pant_price)
    kekai_earnings = total_earnings / 2
    result = kekai_earnings
    return result

print(solution())