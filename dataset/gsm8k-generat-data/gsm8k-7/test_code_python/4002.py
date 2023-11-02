def solution():
    dose = 1000 # in mg
    interval = 6 # in hours
    days = 14
    pill_dosage = 500 # in mg

    # Calculate the total number of doses Jeremy will take
    total_doses = (24 / interval) * days

    # Calculate the number of pills Jeremy will take
    num_pills = total_doses * (dose / pill_dosage)
    result = num_pills
    return result

print(solution())