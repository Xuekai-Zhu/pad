def solution():
    base_pay = 10  # Scout's base pay is $10.00 an hour
    saturday_hours = 4  # Scout worked 4 hours on Saturday
    saturday_customers = 5  # Scout delivered groceries to 5 customers on Saturday
    saturday_earnings = base_pay * saturday_hours + 5 * saturday_customers  # Scout's earnings on Saturday

    sunday_hours = 5  # Scout worked 5 hours on Sunday
    sunday_customers = 8  # Scout delivered groceries to 8 customers on Sunday
    sunday_earnings = base_pay * sunday_hours + 5 * sunday_customers  # Scout's earnings on Sunday

    total_earnings = saturday_earnings + sunday_earnings  # Scout's total earnings over the weekend
    result = total_earnings
    return result

print(solution())