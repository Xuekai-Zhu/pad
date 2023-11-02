def solution():
    num_students = 200
    fraction_look_up = 3/4

    # Each student has 2 eyes, so the total number of eyes is twice the number of students
    total_num_eyes = num_students * 2

    # Calculate the number of eyes that looked up at the airplane
    num_eyes_look_up = total_num_eyes * fraction_look_up

    result = num_eyes_look_up
    return result

print(solution())