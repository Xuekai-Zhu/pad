def solution():
    # Define whether the US President is in the executive branch and has veto power
    us_president_in_executive_branch = True
    us_president_has_veto_power = True
    # Check if the branch with military power also has veto power
    if us_president_in_executive_branch and not us_president_has_veto_power:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())