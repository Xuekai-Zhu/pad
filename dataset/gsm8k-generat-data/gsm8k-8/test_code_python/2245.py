def solution():
    # Define the initial number of lions and the number of months in a year
    initial_lions = 100
    months_in_year = 12

    # Calculate the change in the number of lions each month
    monthly_change = 5 - 1

    # Calculate the final number of lions after one year
    final_lions = initial_lions + (monthly_change * months_in_year)

    result = final_lions
    return result

print(solution())