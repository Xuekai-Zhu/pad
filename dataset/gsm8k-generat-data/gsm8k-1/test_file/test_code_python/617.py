def solution():
    """John injured his back and needs to go to physical therapy. He went to physical therapy for 6 weeks. Each week he went twice for 2 hours at a time. If the sessions cost $125 per hour how much did the physical therapy cost?"""
    weeks = 6
    sessions_per_week = 2
    hours_per_session = 2
    cost_per_hour = 125
    total_cost = weeks * sessions_per_week * hours_per_session * cost_per_hour
    result = total_cost
    return result

print(solution())