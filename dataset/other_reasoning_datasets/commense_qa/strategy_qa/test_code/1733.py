def solution():
    war_to_end_all_wars_ended = 1918
    wehrmacht_start_date = 1935
    if wehrmacht_start_date > war_to_end_all_wars_ended:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())