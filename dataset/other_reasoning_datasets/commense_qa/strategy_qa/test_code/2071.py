def solution():
    jag_air_date = 1995
    joan_crawford_death_date = 1977
    # Joan Crawford could not have guest starred on JAG as she had passed away before the show aired
    if jag_air_date > joan_crawford_death_date:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())