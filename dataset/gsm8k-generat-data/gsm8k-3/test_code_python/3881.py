def solution():
    """Oliver is trying to decide between two different sized boxes of macaroni and cheese. He wants to know which is the better value, so instead of just looking at the overall price, he looks at the price per ounce. The larger box is 30 ounces and the smaller box is 20 ounces. The larger box costs $4.80. The smaller box costs $3.40. What is the price per ounce in cents of the box with the better value (lowest price per ounce)?"""
    # Calculate the price per ounce for each box
    price_per_ounce_1 = 3.40 / 20 * 100  # cents per ounce
    price_per_ounce_2 = 4.80 / 30 * 100  # cents per ounce
    
    # Determine which box has the better value
    if price_per_ounce_1 < price_per_ounce_2:
        result = price_per_ounce_1
    else:
        result = price_per_ounce_2
        
    return result

print(solution())