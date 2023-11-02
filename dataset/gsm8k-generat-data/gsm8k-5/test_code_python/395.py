def solution():
    starting_elefants = 30000  # elephants in the park on Friday evening
    leaving_rate = 2880  # rate of elephant exodus out of the park (elephants/hour)
    leaving_time = 4  # time of elephant exodus (hours)

    # Calculate the number of elephants that left the park during the exodus
    left_during_exodus = leaving_rate * leaving_time

    # Calculate the number of elephants in the park after the exodus
    elephants_after_exodus = starting_elefants - left_during_exodus

    # Calculate the rate of new elephants entering the park
    time_after_exodus = 7  # time after elephant exodus (hours)
    new_elefants_rate = (28980 - elephants_after_exodus) / time_after_exodus

    result = new_elefants_rate
    return result

print(solution())