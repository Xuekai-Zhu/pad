def solution():
    distance = 270 + 180  # total distance to be traveled
    speed = 270 / 3  # speed of the train
    time = distance / speed  # time taken to travel the total distance
    additional_hours = time - 3  # additional hours needed to travel the additional 180 miles
    result = additional_hours
    return result

print(solution())