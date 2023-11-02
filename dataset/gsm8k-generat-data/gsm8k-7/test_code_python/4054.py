def solution():
    upfront_payment = 1000
    hourly_rate = 100
    court_time = 50
    prep_time = 2 * court_time
    brother_contribution = 0.5

    # Calculate the total hours worked by the lawyer
    total_hours = court_time + prep_time

    # Calculate the total amount charged by the lawyer (excluding upfront payment)
    total_charge = total_hours * hourly_rate

    # Calculate the total amount paid by John (excluding brother's contribution)
    john_payment = upfront_payment + total_charge

    # Calculate the total amount paid by both John and his brother
    total_payment = john_payment / brother_contribution

    # Calculate the amount paid by John himself
    john_paid = total_payment * (1 - brother_contribution)
    result = john_paid
    return result

print(solution())