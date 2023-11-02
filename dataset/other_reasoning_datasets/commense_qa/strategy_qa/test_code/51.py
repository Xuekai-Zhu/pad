def solution():
    cycling_impact = "low"
    high_impact_activities = ["long-distance running", "ballet"]
    if cycling_impact not in high_impact_activities:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())