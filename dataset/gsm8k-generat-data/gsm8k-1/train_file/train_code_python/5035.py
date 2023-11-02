def solution():
    """Marlon had 42 lollipops in the beginning. On his way home, he saw Emily and gave her 2/3 of his lollipops. Then, Marlon kept 4 lollipops and gave the rest to Lou. How many lollipops did Lou receive?"""
    initial_lollipops = 42
    emily_share = initial_lollipops * 2/3
    remaining_lollipops = initial_lollipops - emily_share - 4
    lou_share = remaining_lollipops
    result = lou_share
    return result

print(solution())