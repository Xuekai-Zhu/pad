def solution():
    tonight_show_airtime = "11:35PM"
    moonset_time = "9:00PM"
    if tonight_show_airtime > moonset_time:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())