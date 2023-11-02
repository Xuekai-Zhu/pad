def solution():
    
    vampire_drains = 3
    werewolf_eats = 5
    total_people = 72
    weeks = total_people / (vampire_drains + werewolf_eats)
    result = weeks
    return result

print(solution())