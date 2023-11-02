def solution():
    """Elizabeth, Emma, and Elsa went shopping on Wednesday. In total Emma spent $58 If Elsa spent twice as much as Emma, and Elizabeth spent four times as much as Elsa, how much money did they spend in total?"""
    emma_spending = 58
    elsa_spending = 2 * emma_spending
    elizabeth_spending = 4 * elsa_spending
    total_spending = emma_spending + elsa_spending + elizabeth_spending
    result = total_spending
    return result

print(solution())