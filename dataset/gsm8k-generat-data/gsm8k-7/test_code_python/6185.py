def solution():
    refrigerators_per_hr = 90
    coolers_per_hr = refrigerators_per_hr + 70
    hours_per_day = 9
    num_days = 5

    # Calculate the total number of refrigerators produced in 5 days
    total_refrigerators = refrigerators_per_hr * hours_per_day * num_days

    # Calculate the total number of coolers produced in 5 days
    total_coolers = coolers_per_hr * hours_per_day * num_days

    # Calculate the total number of products produced in 5 days
    total_products = total_refrigerators + total_coolers
    result = total_products
    return result

print(solution())