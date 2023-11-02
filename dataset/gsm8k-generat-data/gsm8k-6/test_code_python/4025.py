def solution():
    # Calculate the number of weeks the village of 72 people will last the vampire and werewolf
    total_people = 72
    vampire_drains = 3
    werewolf_eats = 5

    weeks = total_people / (vampire_drains + werewolf_eats)
    result = weeks
    return result

print(solution())