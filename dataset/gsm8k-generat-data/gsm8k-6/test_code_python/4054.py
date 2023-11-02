def solution():
    upfront_fee = 1000  # dollars paid upfront
    court_time = 50  # hours spent in court
    prep_time = 2 * court_time  # hours spent in preparation
    hourly_fee = 100  # dollars charged per hour

    # Calculate the total fee John has to pay
    total_fee = upfront_fee + court_time * hourly_fee + prep_time * hourly_fee
    john_paid = total_fee * 0.5  # John's brother pays half the fee
    result = john_paid
    return result

print(solution())