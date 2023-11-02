def solution():
    """Isabella and Alexis went to the mall to buy some pants and dresses. Alexis bought 3 times more pants and dresses than Isabella. If Alexis bought 21 pairs of pants and 18 dresses, how many pairs of pants and dresses did Isabella buy in total?"""
    alexis_pants = 21
    alexis_dresses = 18
    total_alexis = alexis_pants + alexis_dresses
    isabella_total = total_alexis / 4
    isabella_pants = isabella_total / 2
    isabella_dresses = isabella_total / 2
    result = isabella_total
    
    return result

print(solution())