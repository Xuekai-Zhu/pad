def solution():
    # Define what can be measured with a protractor
    measurable_properties = ["angles"]
    # Check if a caracal can be measured with a protractor
    can_measure_caracal = False
    if any(property in measurable_properties for property in ["length", "width", "weight"]):
        can_measure_caracal = True
    if can_measure_caracal:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())