def solution():
    # Define the ratios of cloves of garlic to number of creatures repelled
    garlic_to_vampires_ratio = 3/2
    garlic_to_vampire_bats_ratio = 3/8
    garlic_to_wights_ratio = 1/3

    # Define the number of creatures to be repelled
    num_vampires = 30
    num_wights = 12
    num_vampire_bats = 40

    # Calculate the total number of cloves of garlic needed
    total_garlic = (num_vampires * garlic_to_vampires_ratio) + (num_wights * garlic_to_wights_ratio) + (num_vampire_bats * garlic_to_vampire_bats_ratio)

    result = total_garlic
    return result

print(solution())