def solution():
    
    trains = 4
    carriages_per_train = 4
    rows_of_wheels_per_carriage = 3
    wheels_per_row = 5
    total_wheels = trains * carriages_per_train * rows_of_wheels_per_carriage * wheels_per_row
    result = total_wheels
    return result

print(solution())