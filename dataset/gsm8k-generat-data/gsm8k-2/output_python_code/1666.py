def solution():
    """Police officer A patrols 36 streets in 4 hours. His colleague, officer B, patrols 55 streets in 5 hours. How many streets will both officers patrol in one hour?"""
    officer_a_streets_per_hour = 36 / 4
    officer_b_streets_per_hour = 55 / 5
    streets_per_hour_together = officer_a_streets_per_hour + officer_b_streets_per_hour
    result = streets_per_hour_together
    return result

print(solution())