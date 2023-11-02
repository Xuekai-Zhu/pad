def solution():
    richard_burton_marriages = {"Elizabeth Taylor": 2, "Sally Burton": 1, "Suzy Hunt": 1, "Sybil Williams": 1}
    clark_gable_marriages = {"Wife 1": 1, "Wife 2": 1, "Wife 3": 1, "Wife 4": 1, "Wife 5": 1}
    # Count the number of one-time marriages for each actor
    rb_one_time_marriages = len([value for value in richard_burton_marriages.values() if value == 1])
    cg_one_time_marriages = len(clark_gable_marriages)
    # Compare the number of one-time marriages for each actor
    if cg_one_time_marriages > rb_one_time_marriages:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())