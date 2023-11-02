def solution():
    # Find out how many cards Jed has after n weeks
    n = 0
    cards = 20
    while cards < 40:
        n += 1
        cards += 6
        if n % 2 == 0:
            cards -= 2
    
    result = n
    return result

print(solution())