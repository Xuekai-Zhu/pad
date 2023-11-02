def solution():
    age_of_dinosaurs = "many millions of years ago"
    start_of_recorded_history = "several thousand years ago"
    if age_of_dinosaurs < start_of_recorded_history:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())