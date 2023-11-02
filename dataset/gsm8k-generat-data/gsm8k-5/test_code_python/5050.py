def solution():
    tablet_price = 450  # The tablet costs $450
    installment_period = 12  # The installment period is 12 months
    down_payment = 100  # The down payment is $100
    installment_price = 40*4 + 35*4 + 30*4  # The total price of the tablet if purchased on installment
    total_price = down_payment + installment_price  # The total price of the tablet if purchased on installment

    # Calculate the amount Loisa will save if she buys the tablet in cash instead of on installment
    savings = total_price - tablet_price
    result = savings
    return result

print(solution())