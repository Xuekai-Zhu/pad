def solution():
    # Define Kirt's initial salary and the percentage increase
    initial_salary = 6000
    increase_percentage = 30

    # Calculate Kirt's salary after one year
    one_year_salary = initial_salary * (1 + increase_percentage/100)

    # Calculate Kirt's total earnings after three years
    total_earnings = one_year_salary * 12 * 3 + initial_salary * 12 * 2

    result = total_earnings
    return result

print(solution())