def solution():
    """Wendy spent 25 years as an accountant and 15 years as an accounting manager. If Wendy lived to be 80 years old, what percentage of her life did she spend in an accounting-related job?"""
    total_years_working = 25 + 15
    total_years_alive = 80
    percentage_working = (total_years_working / total_years_alive) * 100
    result = percentage_working
    return result

print(solution())