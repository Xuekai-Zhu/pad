def solution():
    """Yoque borrowed money from her sister. She promised to pay it back in 11 months including an additional 10% of the money she borrowed. If she pays $15 per month, how much money did she borrow?"""
    # Define the number of months and the monthly payment amount
    num_months = 11
    monthly_payment = 15

    # Define the percentage increase in the borrowed amount
    increase_percentage = 0.1

    # Calculate the total amount paid over the repayment period
    total_paid = num_months * monthly_payment

    # Calculate the original borrowed amount
    borrowed_amount = total_paid / (1 + increase_percentage)

    # Display the borrowed amount
    result = borrowed_amount
    return result

print(solution())