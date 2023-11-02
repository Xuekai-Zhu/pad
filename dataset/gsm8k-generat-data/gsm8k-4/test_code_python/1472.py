def solution():
    """Shara borrowed money from her brother 6 months ago. She returned $10 per month to her brother. Currently, she was able to return half of the money she borrowed. How much will she still owe her brother 4 months from now?"""
    # Define the number of months since Shara borrowed the money and the monthly payment amount
    num_months = 6
    monthly_payment = 10

    # Calculate the total amount borrowed and the amount already paid back
    total_borrowed = num_months * monthly_payment
    amount_paid = total_borrowed / 2

    # Calculate the amount still owed and how much will be left owed in 4 months
    amount_owed = total_borrowed - amount_paid
    amount_owed_in_4_months = amount_owed - (4 * monthly_payment)

    result = amount_owed_in_4_months
    return result

print(solution())