def solution():
    """3 cloves of garlic can repel 2 vampires, 8 vampire bats or 3 wights. How many cloves of garlic are needed to repel 30 vampires, 12 wights and 40 vampire bats?"""
    # Define the number of vampires, vampire bats, and wights
    num_vampires = 30
    num_vampire_bats = 40
    num_wights = 12

    # Define the number of vampires, vampire bats, and wights each 3 cloves of garlic can repel
    vampires_repelled = 2
    vampire_bats_repelled = 8
    wights_repelled = 3

    # Calculate the total number of cloves of garlic needed
    num_cloves = (num_vampires // vampires_repelled) + (num_vampire_bats // vampire_bats_repelled) + (num_wights // wights_repelled)

    # Return the result
    result = num_cloves
    return result

print(solution())