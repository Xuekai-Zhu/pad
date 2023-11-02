def solution():
    """Mike decides to do more pull-ups to increase his strength for climbing. He uses the greasing the groove technique where every time he goes into a certain room he does 2 pull-ups. He decides to use his office. He goes in there 5 times a day every day. How many pull-ups does he do a week?"""
    pull_ups_per_visit = 2
    visits_per_day = 5
    days_per_week = 7
    total_pull_ups = pull_ups_per_visit * visits_per_day * days_per_week
    result = total_pull_ups
    return result

print(solution())