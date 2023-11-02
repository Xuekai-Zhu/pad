def solution():
    earth_day_ceremonies = ["tree plantings", "beach cleanups", "environmental education events"]
    harmful_activities = ["tire fires"]
    overlap = [activity for activity in earth_day_ceremonies if activity in harmful_activities]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())