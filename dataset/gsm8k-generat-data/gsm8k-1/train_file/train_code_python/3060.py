def solution():
    """Mikaela earns $10 an hour tutoring. For the first month, she tutored for 35 hours and in the second month, she tutored 5 hours more than the first month. She spent 4/5 of her total earnings on her personal needs and saved the rest of the money. How much did she save?"""
    rate = 10
    first_month_hours = 35
    second_month_hours = first_month_hours + 5
    total_hours = first_month_hours + second_month_hours
    earnings = rate * total_hours
    personal_needs = earnings * (4/5)
    savings = earnings - personal_needs
    
    result = savings
    return result

print(solution())