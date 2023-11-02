def solution():
    war_year = 1969
    cause_of_war = "rioting during a FIFA Cup qualifying match"
    sport_during_which_cause_occurred = "soccer"
    if sport_during_which_cause_occurred == "soccer":
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())