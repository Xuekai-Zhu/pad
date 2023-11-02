def solution():
    """Kekai's family is having a garage sale. Kekai sells 5 shirts and 5 pairs of pants. Each shirt sells for $1, and each pair of pants sells for $3. If Kekai gives his parents half of the money he earns from selling his clothes, how much money does Kekai have left?"""
    shirt_price = 1
    pants_price = 3
    num_shirts = 5
    num_pants = 5
    total_earned = (shirt_price * num_shirts) + (pants_price * num_pants)
    half_earned = total_earned / 2
    remaining_money = total_earned - half_earned
    result = remaining_money
    return result

print(solution())