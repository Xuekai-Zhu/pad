def solution():
    stargazer_goal = "unknown" # we don't have enough information to determine a preference
    telescope_available = True
    binoculars_available = True
    if telescope_available and not binoculars_available:
        result = "yes"
    elif binoculars_available and not telescope_available:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())