def solution():
    # Calculate the percentage of the original price that Eunice paid
    percentage_paid = 100 - 25
    
    # Calculate the original price of the car using the percentage paid
    original_price = (7500 * 100) / percentage_paid
    
    result = original_price
    return result

print(solution())