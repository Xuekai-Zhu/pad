def solution():
    
    check_amount = 200
    tip_percent = 0.2
    tip_amount = check_amount * tip_percent
    total_amount = check_amount + tip_amount
    friend_contribution = 10
    mark_addition = tip_amount - friend_contribution
    result = mark_addition
    return result

print(solution())