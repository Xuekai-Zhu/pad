def solution():
    religions = ["Hinduism", "Buddhism", "Jainism"]
    origins = {"Hinduism": 500, "Buddhism": 5, "Jainism": 6}
    nineteenth_century_religion = "no"
    for religion in religions:
        if origins[religion] >= 1800:
            nineteenth_century_religion = "yes"
    return nineteenth_century_religion

print(solution())