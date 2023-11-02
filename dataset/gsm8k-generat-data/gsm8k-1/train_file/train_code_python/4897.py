def solution():
    """There are 4 trains waiting at a train station and each train has 4 carriages. Each carriage has 3 rows of wheels and the rows of wheels have 5 wheels each. How many wheels are at the train station?"""
    trains = 4
    carriages_per_train = 4
    rows_of_wheels_per_carriage = 3
    wheels_per_row = 5
    total_wheels = trains * carriages_per_train * rows_of_wheels_per_carriage * wheels_per_row
    result = total_wheels
    return result

print(solution())