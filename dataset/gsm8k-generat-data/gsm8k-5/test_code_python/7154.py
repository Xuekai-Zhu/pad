def solution():
    alexis_pants = 21  # Alexis bought 21 pairs of pants
    alexis_dresses = 18  # Alexis bought 18 dresses
    total_items = alexis_pants + alexis_dresses  # Total number of items bought by Alexis

    # Calculate the ratio of items bought by Isabella and Alexis
    ratio = 1 / 3
    isabella_items = total_items * ratio  # Isabella bought 1/3 of the total items bought by both

    # Calculate the number of pants and dresses Isabella bought
    isabella_pants = isabella_items / 2  # Isabella bought half the number of total items as pants
    isabella_dresses = isabella_items / 2  # Isabella bought half the number of total items as dresses

    # Calculate the total number of pants and dresses Isabella bought
    total_pants_and_dresses = isabella_pants + isabella_dresses
    result = total_pants_and_dresses
    return result

print(solution())