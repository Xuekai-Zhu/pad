def solution():
    requires_electricity = True
    has_power_outage = True
    if requires_electricity and not has_power_outage:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())