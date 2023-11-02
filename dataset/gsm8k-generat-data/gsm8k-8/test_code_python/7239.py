def solution():
    # Define Scout's base pay and tip amount per customer
    base_pay = 10
    tip_per_customer = 5

    # Calculate his earnings on Saturday
    saturday_hours = 4
    saturday_customers = 5
    saturday_earnings = (base_pay * saturday_hours) + (tip_per_customer * saturday_customers)

    # Calculate his earnings on Sunday
    sunday_hours = 5
    sunday_customers = 8
    sunday_earnings = (base_pay * sunday_hours) + (tip_per_customer * sunday_customers)

    # Calculate his total earnings over the weekend
    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())