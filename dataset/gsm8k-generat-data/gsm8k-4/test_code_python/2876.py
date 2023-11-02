def solution():
    """Aaron wants to purchase a guitar under a payment plan of $100.00 per month for 12 months. His father has agreed to lend him the entire amount for the guitar, plus a one-time 10% interest fee for the entire loan. With interest, how much money will Aaron owe his dad?"""
    # Define the cost of the guitar and the monthly payment
    guitar_cost = 1200
    monthly_payment = 100

    # Calculate the interest fee and total amount owed to Aaron's father
    interest_fee = guitar_cost * 0.1
    total_amount_owed = guitar_cost + interest_fee

    # Return the total amount owed after 12 monthly payments
    result = total_amount_owed
    return result

print(solution())