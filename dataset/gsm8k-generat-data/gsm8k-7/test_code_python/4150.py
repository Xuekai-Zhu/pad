def solution():
    incentive = 240

    # Calculate the amount spent on food
    food_spending = incentive * (1/3)
    
    # Calculate the amount spent on clothes
    clothes_spending = incentive * (1/5)
    
    # Calculate the total amount spent
    total_spending = food_spending + clothes_spending
    
    # Calculate the remaining amount
    remaining_amount = incentive - total_spending
    
    # Calculate the amount saved
    amount_saved = remaining_amount * (3/4)
    
    return amount_saved

print(solution())