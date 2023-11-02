def solution():
    current_people = 200
    current_speed = 500
    target_people = 400

    while current_people < target_people:
        current_speed /= 2
        current_people += 100

    result = current_speed
    return result

print(solution())