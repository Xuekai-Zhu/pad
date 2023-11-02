def solution():
    """Winwin won $50 in a lottery. She paid 20% for the tax and she paid $5 for the processing fee. How much was she able to take home?"""
    initial_amount = 50
    tax_percentage = 20
    tax = initial_amount * (tax_percentage / 100)
    processing_fee = 5
    final_amount = initial_amount - tax - processing_fee
    result = final_amount
    return result

print(solution())