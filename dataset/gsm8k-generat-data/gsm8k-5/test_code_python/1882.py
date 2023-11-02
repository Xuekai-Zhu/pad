def solution():
    bananas_left = 100  # There are 100 bananas left after Raj cut some

    # Raj has eaten 70 bananas
    bananas_eaten = 70

    # Raj has twice as many bananas in his basket as the ones left on the tree
    bananas_in_basket = 2 * (bananas_left - bananas_eaten)

    # The total number of bananas on the tree initially
    initial_bananas = bananas_left + bananas_eaten + bananas_in_basket
    result = initial_bananas
    return result

print(solution())