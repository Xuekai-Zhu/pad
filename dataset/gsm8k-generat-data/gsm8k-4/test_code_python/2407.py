def solution():
    """Jane brings 75% as many pieces of bread as treats to feed the live pets at the zoo.
    Wanda brings half as many treats as Jane and three times as many pieces of bread as treats.
    If Wanda brings 90 pieces of bread, what is the total number of pieces of bread and treats that Wanda and Jane brought to the zoo?"""

    # Let's define the variables
    j_treats = None
    j_bread = None
    w_treats = None
    w_bread = 90

    # We know that Wanda brings three times as many pieces of bread as treats,
    # so we divide the bread by 3 to find the number of treats
    w_treats = w_bread / 3

    # We know that Wanda brings half as many treats as Jane,
    # so we double the number of treats to find the number Jane brings
    j_treats = w_treats * 2

    # We know that Jane brings 75% as many pieces of bread as treats,
    # so we multiply the number of treats by 0.75 to find the number of bread
    j_bread = j_treats * 0.75

    # The total number of treats and bread that Wanda and Jane brought is the sum of their individual numbers
    total_treats = w_treats + j_treats
    total_bread = w_bread + j_bread

    # The final result is the sum of total treats and total bread
    result = total_treats + total_bread

    return result

print(solution())