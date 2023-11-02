def solution():
    num_cattle = 340
    original_price = 204000 / num_cattle
    num_sick_cattle = 172
    lowered_price = original_price - 150
    
    # Calculate the number of cattle he can still sell
    remaining_cattle = num_cattle - num_sick_cattle
    
    # Calculate the amount he would have made if he sold all the cattle at original price
    original_amount = num_cattle * original_price
    
    # Calculate the amount he will make by selling the remaining cattle at lowered price
    lowered_amount = remaining_cattle * lowered_price
    
    # Calculate the difference in amount
    loss = original_amount - lowered_amount
    result = loss
    return result

print(solution())