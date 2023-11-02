def solution():
    craton_with_volcanic_activity = ["Laurentia", "Siberia", "Baltica"]
    new_york_harbor_craton = "Laurentia"
    if new_york_harbor_craton in craton_with_volcanic_activity:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())