def solution():
    num_students = 200
    fraction_look_up = 3/4

    # Calculate the number of students who looked up
    num_look_up = num_students * fraction_look_up

    # Calculate the number of eyes that saw the airplane (assuming everyone has 2 eyes)
    num_eyes_saw = num_look_up * 2
    result = num_eyes_saw
    return result

print(solution())