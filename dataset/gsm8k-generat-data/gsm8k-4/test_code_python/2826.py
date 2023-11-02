def solution():
    """Sarah wants to start a cupcake business and was approved for a business loan. The loan has 0% interest if she pays the entire amount back in 5 years, which she decides to do. If she put $10,000 down as a down payment and her monthly payments are $600.00, how much was her loan for (including the down payment)?"""
    
    # Calculate the total number of payments
    total_payments = 5 * 12

    # Calculate the total amount paid through monthly payments
    total_payment_amount = total_payments * 600

    # Calculate the total cost including the down payment
    total_cost = total_payment_amount + 10000

    # return the result
    result = total_cost
    return result

print(solution())