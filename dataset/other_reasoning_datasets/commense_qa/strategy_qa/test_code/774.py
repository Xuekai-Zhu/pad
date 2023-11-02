def solution():
    doctor_strange_creators = ["Steve Ditko", "Stan Lee"]
    batman_creators = ["Bob Kane", "Bill Finger"]
    overlap = [creator for creator in doctor_strange_creators if creator in batman_creators]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())