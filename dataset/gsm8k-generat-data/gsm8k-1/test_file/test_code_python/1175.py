def solution():
    """James has 30 teeth. His dentist drills 4 of them and caps 7 more teeth than he drills. What percentage of James' teeth does the dentist fix?"""
    total_teeth = 30
    drilled_teeth = 4
    capped_teeth = drilled_teeth + 7
    fixed_teeth = drilled_teeth + capped_teeth
    percentage_fixed = (fixed_teeth / total_teeth) * 100
    result = percentage_fixed
    return result

print(solution())