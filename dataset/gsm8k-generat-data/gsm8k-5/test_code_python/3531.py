def solution():
    original_amount = 45  # Nigel won $45
    current_amount = (original_amount + 80) + 10  # Nigel now has $80 more and $10 more than twice the original amount
    twice_original_amount = 2 * original_amount  # Twice the original amount of money Nigel won
    
    # Calculate how much money Nigel gave away
    given_away = (original_amount + 80 + 10) - twice_original_amount
    result = given_away
    return result

print(solution())