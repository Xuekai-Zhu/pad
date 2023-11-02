def solution():
    # Bingley starts with 5 bracelets
    start_bracelets = 5

    # Kelly gives Bingley 1/4 of her 16 bracelets, or 4 bracelets
    bingley_bracelets = start_bracelets + 4

    # Bingley gives 1/3 of his bracelets, or 2 bracelets, to his little sister
    remaining_bracelets = bingley_bracelets - 2

    result = remaining_bracelets
    return result

print(solution())