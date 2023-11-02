def solution():
    """Maximoff's monthly bill is $60 per month. His monthly bill increased by thirty percent when he started working at home. How much is his total monthly bill working from home?"""
    # Define the original bill amount and the percentage increase
    original_bill = 60
    increase_percentage = 30

    # Calculate the new bill amount
    increase_amount = original_bill * (increase_percentage / 100)
    new_bill = original_bill + increase_amount

    # return the result
    result = new_bill
    return result

print(solution())