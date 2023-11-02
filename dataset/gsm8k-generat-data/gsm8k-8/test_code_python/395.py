def solution():
    starting_elefants = 30000
    leaving_rate = 2880
    leaving_time = 4
    entering_time = 7
    final_elefants = 28980

    # Calculate the number of elephants leaving the park
    leaving_elefants = leaving_rate * leaving_time

    # Calculate the number of elephants remaining in the park after the exodus
    remaining_elefants = starting_elefants - leaving_elefants

    # Calculate the rate at which new elephants entered the park
    entering_rate = (final_elefants - remaining_elefants) / entering_time

    result = entering_rate
    return result

print(solution())