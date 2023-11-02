def solution():
    """Hilary is collecting her toenails in a jar to gross out her sister. She can fit 100 toenails in the jar, unless they are from her two big toes, which are twice as big as the rest. She has already filled it with 20 big toenails and 40 regular toenails. How many regular toenails can she fit into the remainder of the jar?"""
    total_toenails = 100
    big_toenail_space = 4
    remaining_space = total_toenails - (20 + big_toenail_space)
    regular_toenails = remaining_space / 2
    result = regular_toenails
    return result

print(solution())