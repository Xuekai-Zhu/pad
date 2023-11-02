def solution():
    # Calculate the amount of money Jenny had before spending
    remaining_money = 24
    spent_money = (3/7) * original_money
    original_money = remaining_money + spent_money
    
    # Calculate half of Jenny's original amount of money
    half_original_money = 0.5 * original_money
    result = half_original_money
    return result

print(solution())