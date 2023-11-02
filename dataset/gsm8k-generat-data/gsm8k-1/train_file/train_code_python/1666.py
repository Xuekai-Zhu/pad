def solution():
    """Police officer A patrols 36 streets in 4 hours. His colleague, officer B, patrols 55 streets in 5 hours. How many streets will both officers patrol in one hour?"""
    streets_per_hour_A = 36/4
    streets_per_hour_B = 55/5
    streets_per_hour_both = streets_per_hour_A + streets_per_hour_B
    result = streets_per_hour_both
    return result

print(solution())