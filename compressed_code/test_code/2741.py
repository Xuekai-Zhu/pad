def solution():
    
    original_amount = 45
    mother_gift = 80
    final_amount = 2 * original_amount + 10
    current_amount = original_amount + mother_gift
    given_away = current_amount - final_amount
    result = given_away
    return result

print(solution())