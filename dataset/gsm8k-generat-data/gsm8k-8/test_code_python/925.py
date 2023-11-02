def solution():
    hours_worked = 8
    customers_per_hour = 7

    ann_customers = hours_worked * customers_per_hour
    becky_customers = hours_worked * customers_per_hour
    julia_customers = 6 * customers_per_hour

    total_customers = ann_customers + becky_customers + julia_customers
    result = total_customers
    return result

print(solution())