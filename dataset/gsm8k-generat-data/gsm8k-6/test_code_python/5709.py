def solution():
    # Calculate the number of cloves of garlic needed to repel 30 vampires, 12 wights and 40 vampire bats
    cloves_per_vampire = 3/2  # 3 cloves repel 2 vampires
    cloves_per_vampire_bat = 3/8  # 3 cloves repel 8 vampire bats
    cloves_per_wight = 1  # 3 cloves repel 3 wights
    total_cloves = cloves_per_vampire * 30 + cloves_per_wight * 12 + cloves_per_vampire_bat * 40
    result = total_cloves
    return result

print(solution())