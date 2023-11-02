def solution():
    winnings = 50
    tax_percent = 0.2
    processing_fee = 5

    # Calculate the amount of tax that Winwin has to pay
    tax_amount = winnings * tax_percent

    # Calculate the amount of money Winwin takes home after paying tax and processing fee
    take_home_amount = winnings - tax_amount - processing_fee
    result = take_home_amount
    return result

print(solution())