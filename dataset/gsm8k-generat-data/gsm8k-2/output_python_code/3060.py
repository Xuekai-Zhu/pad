def solution():
    """Mikaela earns $10 an hour tutoring. For the first month, she tutored for 35 hours and in the second month, she tutored 5 hours more than the first month. She spent 4/5 of her total earnings on her personal needs and saved the rest of the money. How much did she save?"""
    first_month_hours = 35
    second_month_hours = first_month_hours + 5
    hourly_rate = 10
    first_month_earnings = first_month_hours * hourly_rate
    second_month_earnings = second_month_hours * hourly_rate
    total_earnings = first_month_earnings + second_month_earnings
    personal_needs = total_earnings * (4 / 5)
    savings = total_earnings - personal_needs
    result = savings
    return result

print(solution())