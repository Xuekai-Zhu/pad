def solution():
    dancers = 8
    braids_per_dancer = 5
    seconds_per_braid = 30
    minutes_per_braid = seconds_per_braid / 60
    total_braids = dancers * braids_per_dancer
    total_minutes = total_braids * minutes_per_braid
    result = total_minutes
    return result

print(solution())