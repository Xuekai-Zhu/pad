def solution():
    """Oliver is trying to decide between two different sized boxes of macaroni and cheese. He wants to know which is the better value, so instead of just looking at the overall price, he looks at the price per ounce. The larger box is 30 ounces and the smaller box is 20 ounces. The larger box costs $4.80. The smaller box costs $3.40. What is the price per ounce in cents of the box with the better value (lowest price per ounce)?"""
    larger_box_cost = 4.8
    smaller_box_cost = 3.4
    larger_box_size = 30
    smaller_box_size = 20
    larger_box_price_per_ounce = larger_box_cost / larger_box_size
    smaller_box_price_per_ounce = smaller_box_cost / smaller_box_size
    if larger_box_price_per_ounce < smaller_box_price_per_ounce:
        result = int(larger_box_price_per_ounce * 100)
    else:
        result = int(smaller_box_price_per_ounce * 100)
    return result

print(solution())