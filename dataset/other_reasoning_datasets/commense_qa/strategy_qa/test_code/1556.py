def solution():
    pirate_lieutenant_duties = ["in charge of ship", "has many duties"]
    navy_lieutenant_duties = ["second-in-command", "in charge of crew", "has many duties"]
    overlap = [duty for duty in pirate_lieutenant_duties if duty in navy_lieutenant_duties]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())