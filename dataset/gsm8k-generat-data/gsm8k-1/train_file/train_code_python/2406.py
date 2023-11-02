def solution():
    """Jane brings 75% as many pieces of bread as treats to feed the live pets at the zoo. Wanda brings half as many treats as Jane and three times as many pieces of bread as treats. If Wanda brings 90 pieces of bread, what is the total number of pieces of bread and treats that Wanda and Jane brought to the zoo?"""
    wanda_bread = 90
    wanda_treats = (1/2) * ((4/3) * wanda_bread)
    jane_treats = (4/3) * wanda_bread
    jane_bread = (3/4) * jane_treats
    total_treats = wanda_treats + jane_treats
    total_bread = wanda_bread + jane_bread
    result = total_treats + total_bread
    return result

print(solution())