def solution():
    initial_speed = 500
    initial_num_people = 200
    additional_num_people = 200

    num_speed_halvings = additional_num_people / 100

    final_speed = initial_speed / (2 ** num_speed_halvings)
    result = final_speed
    return result

print(solution())