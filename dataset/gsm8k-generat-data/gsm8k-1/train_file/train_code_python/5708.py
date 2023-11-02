def solution():
    """3 cloves of garlic can repel 2 vampires, 8 vampire bats or 3 wights. How many cloves of garlic are needed to repel 30 vampires, 12 wights and 40 vampire bats?"""
    cloves_per_vampire = 3/2
    cloves_per_bat = 3/8
    cloves_per_wight = 3/3
    cloves_needed = (cloves_per_vampire * 30) + (cloves_per_wight * 12) + (cloves_per_bat * 40)
    result = cloves_needed
    return result

print(solution())