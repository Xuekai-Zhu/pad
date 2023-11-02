def solution():
    """Jane brings 75% as many pieces of bread as treats to feed the live pets at the zoo. Wanda brings half as many treats as Jane and three times as many pieces of bread as treats. If Wanda brings 90 pieces of bread, what is the total number of pieces of bread and treats that Wanda and Jane brought to the zoo?"""
    wanda_bread = 90
    wanda_treats = 0.5 * (1 / 0.75) * wanda_bread
    wanda_total = wanda_bread + wanda_treats
    jane_treats = (2 / 3) * wanda_treats
    jane_bread = 0.75 * jane_treats
    jane_total = jane_bread + jane_treats
    total_pieces = wanda_total + jane_total
    result = total_pieces
    return result

print(solution())