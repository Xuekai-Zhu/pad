def solution():
    has_outstanding_achievements = False
    involved_in_flight_safety = False
    warnings_ignored = True
    implicated_in_fatal_explosion = True
    if not warnings_ignored and not implicated_in_fatal_explosion and has_outstanding_achievements and involved_in_flight_safety:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())