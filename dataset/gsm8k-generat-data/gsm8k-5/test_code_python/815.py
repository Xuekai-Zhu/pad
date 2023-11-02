def solution():
    bingley_bracelets = 5  # Bingley starts with 5 bracelets
    kelly_bracelets = 16  # Kelly has 16 bracelets

    # Kelly gives Bingley a fourth of her bracelets
    kelly_gift = kelly_bracelets // 4
    bingley_bracelets += kelly_gift

    # Bingley gives a third of his bracelets to his sister
    sister_gift = bingley_bracelets // 3
    bingley_bracelets -= sister_gift

    result = bingley_bracelets
    return result

print(solution())