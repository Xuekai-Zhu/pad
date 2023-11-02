def solution():
    refrigerators_per_hour = 90
    coolers_per_hour = refrigerators_per_hour + 70
    total_products_per_hour = refrigerators_per_hour + coolers_per_hour

    hours_per_day = 9
    total_hours_worked = 5 * hours_per_day

    total_products = total_products_per_hour * total_hours_worked
    result = total_products
    return result

print(solution())