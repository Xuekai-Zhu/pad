def solution():
    """Marlon had 42 lollipops in the beginning. On his way home, he saw Emily and gave her 2/3 of his lollipops. Then, Marlon kept 4 lollipops and gave the rest to Lou. How many lollipops did Lou receive?"""
    marlon_lollipops = 42
    emily_lollipops = 2/3 * marlon_lollipops
    marlon_lollipops -= emily_lollipops
    marlon_lollipops -= 4
    lou_lollipops = marlon_lollipops
    result = lou_lollipops
    return result

print(solution())