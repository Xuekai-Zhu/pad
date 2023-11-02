def solution():
    # Calculate Janet's income at her current job
    current_income = 30 * 40 * 4  # $30/hour, 40 hours/week, 4 weeks/month

    # Calculate Janet's income as a freelancer
    freelancer_income = (40 - 25) * 40 * 4 - 400  # $40/hour, 40 hours/week, 4 weeks/month, minus taxes and healthcare premiums

    # Calculate the difference in income
    difference = freelancer_income - current_income
    result = difference
    return result

print(solution())