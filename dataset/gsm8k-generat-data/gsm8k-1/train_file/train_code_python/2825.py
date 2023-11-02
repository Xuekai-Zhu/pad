def solution():
    """Sarah wants to start a cupcake business and was approved for a business loan. The loan has 0% interest if she pays the entire amount back in 5 years, which she decides to do. If she put $10,000 down as a down payment and her monthly payments are $600.00, how much was her loan for (including the down payment)?"""
    down_payment = 10000
    monthly_payment = 600
    number_of_payments = 60
    total_amount_paid = down_payment + (monthly_payment * number_of_payments)
    loan_amount = total_amount_paid
    result = loan_amount
    
    return result

print(solution())