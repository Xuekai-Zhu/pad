def solution():
    """Isabella and Alexis went to the mall to buy some pants and dresses. Alexis bought 3 times more pants and dresses than Isabella. If Alexis bought 21 pairs of pants and 18 dresses, how many pairs of pants and dresses did Isabella buy in total?"""
    # Define the number of pants and dresses bought by Alexis
    alexis_pants = 21
    alexis_dresses = 18

    # Calculate the ratio of pants and dresses between Alexis and Isabella
    ratio = 3
    total_ratio = ratio + 1
    isabella_ratio = 1 / total_ratio
    alexis_ratio = ratio / total_ratio

    # Calculate the total number of pants and dresses bought by Isabella
    isabella_pants = isabella_ratio * (alexis_pants + alexis_dresses)
    isabella_dresses = isabella_pants

    # return the result
    result = isabella_pants + isabella_dresses
    return result

print(solution())