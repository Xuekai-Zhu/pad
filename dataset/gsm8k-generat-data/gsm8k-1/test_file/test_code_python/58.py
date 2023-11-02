def solution():
    """If Marcy works for the same company for 40 years, she gets an annual pension of $50,000/year. 
    Starting after 20 years, she becomes entitled to 5% of the value of the pension per year. 
    If she quits after 30 years, what will her annual pension be?"""
    base_pension = 50000
    years_worked = 30
    percentage_increase = 0.05
    years_entitled_to_increase = years_worked - 20
    increase = percentage_increase * years_entitled_to_increase * base_pension
    total_pension = base_pension + increase
    result = total_pension
    return result

print(solution())