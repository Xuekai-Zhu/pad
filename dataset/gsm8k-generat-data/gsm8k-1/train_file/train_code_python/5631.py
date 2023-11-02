def solution():
    """Tom is binge-watching a show on Netflix. The show has 90 episodes, each one of which is 20 minutes long because there are no commercials. If Tom can spend two hours a day watching the show, how many days will it take him to finish watching the show?"""
    total_minutes = 90 * 20
    minutes_per_day = 2 * 60
    days_to_finish = total_minutes / minutes_per_day
    result = days_to_finish
    return result

print(solution())