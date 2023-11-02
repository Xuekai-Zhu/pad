def solution():
    total_aprons = 150
    already_sewn = 13
    todays_sewn = 3 * already_sewn

    # Calculate the number of remaining aprons needed to be sewn
    remaining_aprons = total_aprons - already_sewn - todays_sewn

    # Calculate the number of aprons to be sewn tomorrow
    aprons_to_sew_tomorrow = remaining_aprons / 2
    result = aprons_to_sew_tomorrow
    return result

print(solution())