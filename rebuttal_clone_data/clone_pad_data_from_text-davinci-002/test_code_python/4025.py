def solution():
    vampires = 3
    werewolves = 5
    village = 72
    week = 0
    while village > 0:
        if vampires <= werewolves:
            village -= vampires
            vampires = 0
        else:
            village -= werewolves
            vampires -= werewolves
        werewolves = 0
        week += 1
    return week

print(solution())