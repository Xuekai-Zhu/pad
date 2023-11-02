def solution():
    desperate_housewives_episodes = 180
    lois_and_clark_episodes = 87
    twice_as_many = lois_and_clark_episodes * 2
    if desperate_housewives_episodes > twice_as_many:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())