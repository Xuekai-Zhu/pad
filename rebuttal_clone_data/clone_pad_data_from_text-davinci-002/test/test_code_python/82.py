def solution():
    
    initial_amount = 50
    tax_percentage = 20
    tax = initial_amount * (tax_percentage / 100)
    processing_fee = 5
    final_amount = initial_amount - tax - processing_fee
    result = final_amount
    return result

print(solution())