def solution():
    initial_salary = 6000  # Kirt has a $6000 monthly salary when he started his job
    increase = 0.3  # His salary increased by 30%
    duration = 3  # Kirt worked for 3 years

    # Calculate Kirt's total earnings after 3 years
    total_earnings = initial_salary * (1 + increase) ** duration * 12
    result = total_earnings
    return result

print(solution())