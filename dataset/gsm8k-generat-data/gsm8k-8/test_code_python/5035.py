def solution():
    # Define the initial investment
    initial_investment = 300

    # Calculate the interest earned in the first month
    first_month_interest = initial_investment * 0.1

    # Calculate the total at the end of the first month
    total_first_month = initial_investment + first_month_interest

    # Calculate the interest earned in the second month
    second_month_interest = total_first_month * 0.1

    # Calculate the total at the end of the second month
    total_second_month = total_first_month + second_month_interest

    result = total_second_month
    return result

print(solution())