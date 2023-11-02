def solution():
    initial_amount = 55  # initial amount in Lily's account
    spent_on_shirt = 7  # amount spent on a shirt
    spent_on_other_shop = 3 * spent_on_shirt  # three times the amount spent on a shirt
    
    # Calculate the remaining amount in Lily's account
    remaining_amount = initial_amount - spent_on_shirt - spent_on_other_shop
    result = remaining_amount
    return result

print(solution())