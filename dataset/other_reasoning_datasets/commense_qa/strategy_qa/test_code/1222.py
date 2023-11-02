def solution():
    mill_power_source = "hydropower"
    does_hydropower_produce_chaff = True
    if mill_power_source == "hydropower" and does_hydropower_produce_chaff:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())