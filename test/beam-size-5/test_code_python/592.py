def solution():
    num_implants = 2
    base_price = 2000
    feature_cost = 500
    deposit = 600
    hourly_rate = 15

    # Calculate the total cost of all implants
    total_cost = num_implants * base_price + feature_cost

    # Calculate the total amount George has already earned
    total_earned = total_cost + deposit

    # Calculate the number of hours George needs to work to pay for the dental work
    hours_needed = total_earned / hourly_rate
    result = hours_needed
    return result

print(solution())