def solution():
    final_price = 7500  # Eunice spent $7500 on the car
    discount_percentage = 25  # The car was sold at a discount of 25%
    
    # Calculate the original price of the car
    original_price = final_price / (1 - (discount_percentage/100))
    
    result = original_price
    return result

print(solution())