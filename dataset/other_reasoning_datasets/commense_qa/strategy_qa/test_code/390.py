def solution():
    eid_duration = 3  # maximum duration of Eid al-Fitr in days
    office_duration = (4*24) + 3 + (30/60) # convert total duration to hours
    if office_duration > (eid_duration*24):
        result = "yes, it is inappropriate"
    else:
        result = "no, it is not inappropriate"
    return result

print(solution())