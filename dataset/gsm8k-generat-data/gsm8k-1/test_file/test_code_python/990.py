def solution():
    """Tobias, Chikote, and Igneous are the three little wolves who live in the forest and howl at the moon every night.
    When Tobias howls, each howl lasts for a total of 20 seconds. Chikote howls for twice as long as Tobias. And Igneous howls 
    for as long as the other two wolves combined. What is the combined length of time, in minutes, of the three wolves' howls?"""
    tobias_howl = 20
    chikote_howl = tobias_howl * 2
    igneous_howl = (tobias_howl + chikote_howl)
    total_howl_time = (tobias_howl + chikote_howl + igneous_howl) / 60
    result = total_howl_time
    return result

print(solution())