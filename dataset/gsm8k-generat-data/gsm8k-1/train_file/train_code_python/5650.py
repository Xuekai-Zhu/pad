def solution():
    """Nathan bought one large box of bananas. He saw that there are six bunches with eight bananas in a bunch and five bunches with seven bananas in a bunch. How many bananas did Nathan have?"""
    bunches_of_eights = 6
    bananas_per_bunch_of_eights = 8
    bunches_of_sevens = 5
    bananas_per_bunch_of_sevens = 7
    total_bananas = (bunches_of_eights * bananas_per_bunch_of_eights) + (bunches_of_sevens * bananas_per_bunch_of_sevens)
    result = total_bananas
    return result

print(solution())