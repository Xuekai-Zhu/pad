def solution():
    current_sales = 4000  # The shoe company currently sells $4000 worth of shoes every month
    target_income = 60000  # The shoe company wants to make $60000 in a year
    months_in_a_year = 12  # There are 12 months in a year

    # Calculate the difference between the current income and the target income
    income_difference = target_income - (current_sales * months_in_a_year)

    # Calculate the additional amount of sales the company needs to make each month
    additional_sales_per_month = income_difference / months_in_a_year
    result = additional_sales_per_month
    return result

print(solution())