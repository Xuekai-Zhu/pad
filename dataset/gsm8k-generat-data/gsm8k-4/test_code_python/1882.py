def solution():
    """A banana tree has 100 bananas left after Raj cut some bananas from it. If Raj has eaten 70 bananas and has twice as many remaining in his basket, how many bananas were on the tree initially?"""
    # Define the number of bananas left on the tree
    bananas_left = 100

    # Calculate the number of bananas Raj had in his basket
    raj_basket = (bananas_left - 70) * 2

    # Calculate the number of bananas on the tree initially
    initial_bananas = raj_basket + bananas_left

    result = initial_bananas
    return result

print(solution())