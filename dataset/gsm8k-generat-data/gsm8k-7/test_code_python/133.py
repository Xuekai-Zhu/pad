def solution():
    num_students = 40
    absent_fraction = 1 / 10
    present_fraction = 1 - absent_fraction
    classroom_fraction = 3 / 4
    canteen_fraction = 1 - classroom_fraction

    # Calculate the number of students who are present
    num_present = num_students * present_fraction

    # Calculate the number of students who are in the classroom
    num_classroom = num_present * classroom_fraction

    # Calculate the number of students who are in the canteen
    num_canteen = num_present * canteen_fraction
    result = num_canteen
    return result

print(solution())