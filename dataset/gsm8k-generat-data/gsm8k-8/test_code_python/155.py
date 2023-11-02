def solution():
    # Calculate the number of mangoes sold to the market
    mangoes_market = 20 * 8

    # Calculate the number of mangoes sold to his community
    mangoes_community = (60 - 20) / 2 * 8

    # Calculate the total number of mangoes he still has
    mangoes_remaining = mangoes_market + mangoes_community
    result = mangoes_remaining
    return result

print(solution())