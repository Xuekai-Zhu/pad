def solution():
    
    bingley_bracelets = 5
    kelly_bracelets = 16
    kelly_gives = kelly_bracelets // 4
    bingley_bracelets += kelly_gives
    bingley_gives = bingley_bracelets // 3
    bingley_bracelets -= bingley_gives
    result = bingley_bracelets
    return result

print(solution())