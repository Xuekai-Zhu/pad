def solution():
    bingley_bracelets = 5
    kelly_bracelets = 16
    given_bracelets = kelly_bracelets / 4
    bingley_bracelets = bingley_bracelets + given_bracelets
    bracelets_given = bingley_bracelets / 3
    bingley_bracelets = bingley_bracelets - bracelets_given
    result = bingley_bracelets
    
    return result

print(solution())