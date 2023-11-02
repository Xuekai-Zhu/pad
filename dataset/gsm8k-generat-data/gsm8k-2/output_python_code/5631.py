def solution():
    """Tom is binge-watching a show on Netflix. The show has 90 episodes, each one of which is 20 minutes long because there are no commercials. If Tom can spend two hours a day watching the show, how many days will it take him to finish watching the show?"""
    total_time_in_minutes = 90 * 20
    days_to_watch = total_time_in_minutes / (2 * 60)
    result = days_to_watch
    return result

print(solution())