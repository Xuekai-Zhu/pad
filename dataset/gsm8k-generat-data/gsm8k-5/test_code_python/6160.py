def solution():
    cash_price = 8000  # The cash price of the refrigerator is $8000
    deposit = 3000  # Samantha pays a deposit of $3000
    monthly_installment = 300  # Samantha pays $300 each month for 30 months

    # Calculate the total amount Samantha will pay if she pays in installments
    total_installment_price = deposit + (monthly_installment * 30)

    # Calculate how much money Samantha would have saved by paying cash
    savings = cash_price - total_installment_price
    result = savings
    return result

print(solution())