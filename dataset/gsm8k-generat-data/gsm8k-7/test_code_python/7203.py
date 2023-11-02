def solution():
    first_8_customers = 8 * 3
    next_4_customers = 4 * 2
    last_8_customers = 8 * 1

    # Calculate the total number of cases of cat food sold
    total_cases_sold = first_8_customers + next_4_customers + last_8_customers
    result = total_cases_sold
    return result

print(solution())