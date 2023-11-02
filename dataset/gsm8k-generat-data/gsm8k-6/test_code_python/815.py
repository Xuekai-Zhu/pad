def solution():
    # Calculate the number of bracelets Bingley will have after receiving a fourth of Kelly's bracelets
    bingley_bracelets = 5
    kelly_bracelets = 16
    bingley_bracelets += kelly_bracelets/4

    # Calculate the number of bracelets Bingley will have after giving a third to his sister
    bingley_bracelets -= bingley_bracelets/3

    result = bingley_bracelets
    return result

print(solution())