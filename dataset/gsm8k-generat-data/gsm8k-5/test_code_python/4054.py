def solution():
    upfront_fee = 1000  # John pays $1000 upfront
    court_hours = 50  # The lawyer works 50 hours in court time
    prep_hours = 2 * court_hours  # The lawyer spends twice as much time in prep time

    # Calculate the total fee without including his brother's payment
    total_fee = upfront_fee + (100 * (court_hours + prep_hours))

    # Calculate the payment made by John's brother
    brother_payment = total_fee / 2

    # Calculate the total payment made by John
    john_payment = upfront_fee + (100 * court_hours) + (100 * prep_hours) - brother_payment
    result = john_payment
    return result

print(solution())