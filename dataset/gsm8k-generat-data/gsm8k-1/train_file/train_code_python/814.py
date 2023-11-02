def solution():
    """Bingley has 5 bracelets. Kelly gives Bingley a fourth of her 16 bracelets. Then Bingley gives a third of his bracelets to his little sister. How many bracelets does Bingley have remaining?"""
    bingley_bracelets = 5
    kelly_bracelets = 16
    kelly_gives = kelly_bracelets // 4
    bingley_bracelets += kelly_gives
    bingley_gives = bingley_bracelets // 3
    bingley_bracelets -= bingley_gives
    result = bingley_bracelets
    return result

print(solution())