def solution():
    # Determine Maya's initial lift
    maya_initial_lift = 240 * 1/4

    # Determine Maya's peak lift
    maya_peak_lift = 300 * 1/2

    # Determine how many times Maya's lift increased
    increase = (maya_peak_lift - maya_initial_lift) / 10

    # Calculate Maya's current lift
    maya_current_lift = maya_initial_lift + (increase * 10)

    # Calculate the difference in Maya's lift from the beginning to now
    difference = maya_current_lift - maya_initial_lift
    result = difference
    return result

print(solution())