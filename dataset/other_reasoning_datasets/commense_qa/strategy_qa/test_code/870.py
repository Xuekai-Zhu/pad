def solution():
    eastenders_episodes = 6000
    binge_watching_days = 125
    human_water_survival_days = 4
    total_water_needed = human_water_survival_days * eastenders_episodes / binge_watching_days
    if total_water_needed == 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())