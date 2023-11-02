def solution():
    james_brown_ex_wives = 4
    players_per_team = 2
    if james_brown_ex_wives >= players_per_team * 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())