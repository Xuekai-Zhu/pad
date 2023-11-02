def solution():
    annual_earnings = 5000000
    total_female_employees = 2/3 * 3300
    total_female_mothers = total_female_employees - 1200
    bonus_percentage = 0.25

    # Calculate the total bonus amount
    total_bonus = annual_earnings * bonus_percentage

    # Calculate the bonus amount for each female mother employee
    bonus_per_employee = total_bonus / total_female_mothers
    result = bonus_per_employee
    return result

print(solution())