def solution():
    steps_across_floor = 30
    floors_ descended = 9
    steps_taken = floors_descended * steps_across_floor
    elevator_time = 60
    stairs_time = steps_taken / 3
    result = elevator_time - stairs_time
    return result

print(solution())