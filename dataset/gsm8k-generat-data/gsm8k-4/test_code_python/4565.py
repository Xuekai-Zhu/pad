def solution():
    """Yoque borrowed money from her sister. She promised to pay it back in 11 months including an additional 10% of the money she borrowed. If she pays $15 per month, how much money did she borrow?"""
    # Define the number of months and the monthly payment
    months = 11
    monthly_payment = 15

    # Calculate the total amount paid over the 11 months
    total_paid = months * monthly_payment

    # Calculate the amount borrowed using the total paid and the 10% additional payment
    amount_borrowed = total_paid / 1.1

    # round the result to two decimal places
    result = round(amount_borrowed, 2)
    return result

print(solution())