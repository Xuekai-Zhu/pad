def solution():
    
    distance_to_destination = 2/3
    time_sailed_due_east = 20
    speed_sailed_due_east = 30
    distance_sailed_due_east = time_sailed_due_east * speed_sailed_due_east
    distance_blown_westward = distance_sailed_due_east - distance_to_destination * distance_sailed_due_east
    result = distance_blown_westward
    return result

print(solution())