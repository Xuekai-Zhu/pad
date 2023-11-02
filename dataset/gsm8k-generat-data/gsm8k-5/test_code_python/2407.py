def solution():
    wanda_bread = 90  # Wanda brings 90 pieces of bread
    wanda_treats = (1/2) * (wanda_bread/3)  # Wanda brings half as many treats as Jane and three times as many pieces of bread as treats
    jane_treats = (4/3) * wanda_treats  # Jane brings 75% as many pieces of bread as treats

    # Calculate the total number of pieces of bread and treats brought by Jane and Wanda
    total_bread = wanda_bread + (3/4) * jane_treats  # Jane brings 75% as many pieces of bread as treats
    total_treats = wanda_treats + jane_treats
    result = total_bread + total_treats
    return result

print(solution())