def solution():
    """Randy has $200 in his piggy bank. He spends 2 dollars every time he goes to the store. He makes 4 trips to the store every month. How much money, in dollars, will be in his piggy bank after a year?"""
    starting_amount = 200
    monthly_spending = 2 * 4
    remaining_amount = starting_amount - monthly_spending
    remaining_amount_per_year = remaining_amount * 12
    result = remaining_amount_per_year
    return result

print(solution())