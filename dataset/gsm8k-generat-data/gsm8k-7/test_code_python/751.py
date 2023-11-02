def solution():
    monday_speed = 10 # meters per hour

    # Calculate the speeds on Tuesday - Thursday
    tue_thu_speed = monday_speed * 1.5

    # Calculate the speed on Friday
    fri_speed = tue_thu_speed * 1.6

    result = fri_speed
    return result

print(solution())