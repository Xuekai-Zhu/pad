def solution():
    rand_paul_positions = ["electronic fence and no amnesty", "undocumented immigrants granted legal status"]
    if len(set(rand_paul_positions)) > 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())