def solution():
    base_pay = 10.00
    per_customer_tip = 5.00
    hours_worked_sat = 4
    customers_sat = 5
    hours_worked_sun = 5
    customers_sun = 8
    total_hours = hours_worked_sat + hours_worked_sun
    total_customers = customers_sat + customers_sun
    total_pay = (base_pay * total_hours) + (total_customers * per_customer_tip)
    result = total_pay
    return result

print(solution())