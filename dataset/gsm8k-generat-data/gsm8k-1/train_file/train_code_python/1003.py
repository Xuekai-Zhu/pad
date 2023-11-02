def solution():
    """Kamil wants to renovate his kitchen at home. For this purpose, he hired two professionals who work for him 6 hours a day for 7 days. What does it cost Kamil to hire these professionals if one of them is paid $15 per hour of work?"""
    hours_per_day = 6
    days = 7
    num_professionals = 2
    rate_per_hour = 15
    total_hours = hours_per_day * days * num_professionals
    total_cost = total_hours * rate_per_hour
    result = total_cost
    return result

print(solution())