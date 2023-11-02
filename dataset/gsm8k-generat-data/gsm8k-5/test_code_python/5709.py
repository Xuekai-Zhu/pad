def solution():
    garlic_vs_vampires = 3/2  # 3 cloves of garlic can repel 2 vampires
    garlic_vs_bats = 3/8  # 3 cloves of garlic can repel 8 vampire bats
    garlic_vs_wights = 1  # 3 cloves of garlic can repel 3 wights

    # Calculate how many cloves of garlic are needed to repel 30 vampires
    cloves_for_vampires = (30/2) * garlic_vs_vampires

    # Calculate how many cloves of garlic are needed to repel 12 wights
    cloves_for_wights = 12 * garlic_vs_wights

    # Calculate how many cloves of garlic are needed to repel 40 vampire bats
    cloves_for_bats = (40/8) * garlic_vs_bats

    # Calculate the total number of cloves of garlic needed
    total_cloves = cloves_for_vampires + cloves_for_wights + cloves_for_bats
    result = total_cloves
    return result

print(solution())