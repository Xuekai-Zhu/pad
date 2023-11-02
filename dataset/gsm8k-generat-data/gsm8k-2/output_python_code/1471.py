def solution():
    """Shara borrowed money from her brother 6 months ago. She returned $10 per month to her brother. Currently, she was able to return half of the money she borrowed. How much will she still owe her brother 4 months from now?"""
    total_borrowed = 6 * 10  # Shara borrowed $60
    total_returned = 30  # Shara returned half of the total borrowed ($60/2)
    remaining_borrowed = total_borrowed - total_returned  # Shara still owes $30
    remaining_months = 4  # Shara will still owe the money in 4 months
    monthly_payment = 10  # Shara pays $10 per month
    remaining_debt = remaining_borrowed - (monthly_payment * remaining_months)  # Shara will still owe $10 after 4 months
    result = remaining_debt
    return result

print(solution())