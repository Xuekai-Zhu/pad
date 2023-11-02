def solution():
    states_exempt_from_pledge = ["California", "Hawaii", "Iowa", "Vermont", "Wyoming"]
    jackson_pollock_parents_hometown = "Tingley, Iowa"
    if jackson_pollock_parents_hometown in states_exempt_from_pledge:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())