def solution():
    """Elizabeth, Emma, and Elsa went shopping on Wednesday. In total Emma spent $58 If Elsa spent twice as much as Emma, and Elizabeth spent four times as much as Elsa, how much money did they spend in total?"""
    emma_spent = 58
    elsa_spent = emma_spent * 2
    elizabeth_spent = elsa_spent * 4
    total_spent = emma_spent + elsa_spent + elizabeth_spent
    result = total_spent
    return result

print(solution())