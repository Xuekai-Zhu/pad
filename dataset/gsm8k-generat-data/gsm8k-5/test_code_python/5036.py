def solution():
    # Marlon had 42 lollipops in the beginning
    initial_lollipops = 42

    # Marlon gave Emily 2/3 of his lollipops
    emily_lollipops = (2/3) * initial_lollipops

    # Marlon kept 4 lollipops
    marlon_lollipops = 4

    # Marlon gave the rest to Lou
    lou_lollipops = initial_lollipops - emily_lollipops - marlon_lollipops
    result = lou_lollipops
    return result

print(solution())