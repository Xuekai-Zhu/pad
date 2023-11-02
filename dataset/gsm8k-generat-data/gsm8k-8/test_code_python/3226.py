def solution():
    friday_customers = 28
    saturday_customers = 3 * friday_customers
    sunday_customers = 36

    total_customers = friday_customers + saturday_customers + sunday_customers
    total_tips = total_customers * 2

    result = total_tips
    return result

print(solution())