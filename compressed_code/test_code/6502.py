def solution():
    
    hours_per_day = 8
    ann_customers = 7 * hours_per_day
    becky_customers = 7 * hours_per_day
    julia_customers = 7 * 6
    total_customers = ann_customers + becky_customers + julia_customers
    result = total_customers
    return result

print(solution())