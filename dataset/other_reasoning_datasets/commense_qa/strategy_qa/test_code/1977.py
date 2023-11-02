def solution():
    metric_units = ["meter", "centimeter", "kilometer"]
    american_units = ["foot", "inch", "yard"]
    overlap = [unit for unit in metric_units if unit in american_units]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())