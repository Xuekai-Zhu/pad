def solution():
    weekly_allowance = 30
    junk_food_spending = weekly_allowance / 3
    sweets_spending = 8
    
    # Calculate the total amount spent on junk food and sweets
    total_spending = junk_food_spending + sweets_spending
    
    # Calculate the amount saved
    amount_saved = weekly_allowance - total_spending
    result = amount_saved
    return result

print(solution())