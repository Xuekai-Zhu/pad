def solution():
    """Isabella and Alexis went to the mall to buy some pants and dresses. Alexis bought 3 times more pants and dresses than Isabella. If Alexis bought 21 pairs of pants and 18 dresses, how many pairs of pants and dresses did Isabella buy in total?"""
    # Calculate the total number of pants and dresses Alexis bought
    alexis_pants = 21
    alexis_dresses = 18
    total_alexis = alexis_pants + alexis_dresses

    # Calculate the number of pants and dresses Isabella bought
    isabella_total = total_alexis / 4
    isabella_pants = isabella_total / 2
    isabella_dresses = isabella_total / 2

    # Display the total number of pants and dresses Isabella bought
    result = isabella_total
    return result, isabella_pants, isabella_dresses

print(solution())