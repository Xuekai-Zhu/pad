def solution():
    """Oliver is trying to decide between two different sized boxes of macaroni and cheese. He wants to know which is the better value, so instead of just looking at the overall price, he looks at the price per ounce. The larger box is 30 ounces and the smaller box is 20 ounces. The larger box costs $4.80. The smaller box costs $3.40. What is the price per ounce in cents of the box with the better value (lowest price per ounce)?"""
    # Calculate the price per ounce for both boxes
    price_per_ounce_large = 4.8 / 30
    price_per_ounce_small = 3.4 / 20

    # Determine which box has the lower price per ounce
    if price_per_ounce_large < price_per_ounce_small:
        best_value = "larger box"
        price_per_ounce = price_per_ounce_large
    else:
        best_value = "smaller box"
        price_per_ounce = price_per_ounce_small

    # Convert the price per ounce to cents
    price_per_ounce_cents = price_per_ounce * 100

    result = price_per_ounce_cents
    return result

print(solution())