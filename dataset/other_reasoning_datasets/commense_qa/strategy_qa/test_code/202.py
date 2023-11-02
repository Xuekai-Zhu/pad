def solution():
    mortality_rate = 0.06
    completion_rate = 0.0 # assuming no one completes the action due to pain or shock
    if completion_rate == 0 or (mortality_rate / completion_rate) < 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())