def solution():
    base_pay = 10
    tip_per_customer = 5

    saturday_hours = 4
    saturday_customers = 5

    sunday_hours = 5
    sunday_customers = 8

    # Calculate the total tip for Saturday
    saturday_tip = tip_per_customer * saturday_customers

    # Calculate the total pay for Saturday
    saturday_pay = base_pay * saturday_hours

    # Calculate the total tip for Sunday
    sunday_tip = tip_per_customer * sunday_customers

    # Calculate the total pay for Sunday
    sunday_pay = base_pay * sunday_hours

    # Calculate the total pay for the weekend
    total_pay = saturday_pay + sunday_pay + saturday_tip + sunday_tip
    result = total_pay
    return result

print(solution())