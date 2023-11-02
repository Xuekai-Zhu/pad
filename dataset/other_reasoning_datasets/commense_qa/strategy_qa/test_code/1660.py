def solution():
    bear_label = "Cub"
    scout_labels = ["Cub Scouts", "Eagle Scouts"]
    if bear_label in scout_labels:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())