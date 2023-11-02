def solution():
    num_inexperienced_sailors = 5
    experienced_salary_ratio = 1.2 # Experienced sailors are paid 1/5 times more than inexperienced sailors, so their salary ratio is 1 + 1/5 = 1.2
    inexperienced_salary = 10 * 60 # Inexperienced sailors earn $10 per hour for a 60-hour workweek
    total_inexperienced_pay = num_inexperienced_sailors * inexperienced_salary

    # Calculate the total pay of all sailors
    total_sailor_pay = total_inexperienced_pay / (1 + num_inexperienced_sailors * (experienced_salary_ratio - 1))
    # Divide by the ratio of total pay between inexperienced and experienced sailors

    # Calculate the pay of experienced sailors
    experienced_pay = total_sailor_pay - total_inexperienced_pay

    # Calculate the total combined monthly earnings of the experienced sailors
    total_experienced_earnings = experienced_pay * 4 # Assuming a 4-week month

    result = total_experienced_earnings
    return result

print(solution())