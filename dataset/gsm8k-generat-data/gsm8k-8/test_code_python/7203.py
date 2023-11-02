def solution():
    # Calculate the number of cases sold by the first 8 customers
    first_8_customers_cases = 8 * 3

    # Calculate the number of cases sold by the next 4 customers
    next_4_customers_cases = 4 * 2

    # Calculate the number of cases sold by the last 8 customers
    last_8_customers_cases = 8 * 1

    # Calculate the total number of cases sold
    total_cases_sold = first_8_customers_cases + next_4_customers_cases + last_8_customers_cases
    result = total_cases_sold
    return result

print(solution())