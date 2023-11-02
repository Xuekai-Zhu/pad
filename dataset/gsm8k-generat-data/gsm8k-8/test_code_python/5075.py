def solution():
    # Calculate the number of times the $100/$10 discount applies
    discount_count = 250 // 100
    
    # Calculate the total amount of discount received
    discount_amount = discount_count * 10
    
    # Calculate the final amount paid
    final_amount = 250 - discount_amount
    result = final_amount
    return result

print(solution())