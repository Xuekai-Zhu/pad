def solution():
    # Calculate the total number of walnuts the boy squirrel brought to the burrow
    boy_walnuts = 6
    dropped_walnuts = 1
    total_boy_walnuts = boy_walnuts - dropped_walnuts

    # Calculate the total number of walnuts in the burrow after the boy squirrel's contribution
    total_burrow_walnuts = total_boy_walnuts + 12

    # Calculate the total number of walnuts in the burrow after the girl squirrel's contribution
    girl_walnuts = 5
    eaten_walnuts = 2
    total_girl_walnuts = girl_walnuts - eaten_walnuts
    final_total_walnuts = total_burrow_walnuts + total_girl_walnuts
    result = final_total_walnuts
    return result

print(solution())