def solution():
    total_people = 100  # There are 100 people in the theater
    blue_eyes = 19  # 19 people have blue eyes
    brown_eyes = total_people / 2  # Half of the people have brown eyes
    black_eyes = total_people / 4  # A quarter of the people have black eyes

    # Calculate the number of people who have green eyes
    green_eyes = total_people - blue_eyes - brown_eyes - black_eyes
    result = green_eyes
    return result

print(solution())