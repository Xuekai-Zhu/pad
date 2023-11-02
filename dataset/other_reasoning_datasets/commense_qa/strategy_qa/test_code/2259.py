def solution():
    futurama_episodes = 140
    simpsons_episodes = 600
    years_since_futurama_cancelled = 7
    futurama_average_episodes_per_year = futurama_episodes / years_since_futurama_cancelled
    futurama_predicted_episodes_by_end_of_2020 = futurama_episodes + futurama_average_episodes_per_year
    if futurama_predicted_episodes_by_end_of_2020 > simpsons_episodes:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())