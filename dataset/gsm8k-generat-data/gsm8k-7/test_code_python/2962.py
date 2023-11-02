def solution():
    hourly_wage = 15
    ride_payment = 5
    good_review_bonus = 20
    gas_price = 3
    gas_amount = 17

    # Calculate the total payment for rides given
    total_ride_payment = ride_payment * 3

    # Calculate the total bonus for good reviews
    total_review_bonus = good_review_bonus * 2

    # Calculate the total earned for hours worked
    total_hourly_payment = hourly_wage * 8

    # Calculate the total cost for gas
    total_gas_cost = gas_price * gas_amount

    # Calculate the total earned for the day
    total_earned = total_ride_payment + total_review_bonus + total_hourly_payment + total_gas_cost

    result = total_earned
    return result

print(solution())