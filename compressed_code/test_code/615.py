def solution():
    
    bingley_bracelets = 5
    kelly_bracelets = 16
    bingley_bracelets += kelly_bracelets / 4
    bingley_bracelets -= bingley_bracelets / 3
    result = bingley_bracelets
    return result

print(solution())