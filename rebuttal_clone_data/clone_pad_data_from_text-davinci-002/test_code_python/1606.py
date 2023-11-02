def solution():
    america_lift = 240
    maya_lift = america_lift / 4
    maya_lift_increase = 10
    maya_peak_lift = 300
    america_peak_lift = maya_peak_lift * 2
    maya_lift_now = america_peak_lift / 2
    maya_lift_difference = maya_lift_now - maya_lift
    result = maya_lift_difference
    return result

print(solution())