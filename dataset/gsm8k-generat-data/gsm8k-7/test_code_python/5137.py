def solution():
    fifth_graders = 109
    sixth_graders = 115
    seventh_graders = 118
    num_teachers_per_grade = 4
    num_parents_per_grade = 2
    num_seats_per_bus = 72

    # Calculate the total number of students and chaperones
    total_people = fifth_graders + sixth_graders + seventh_graders + \
        (num_teachers_per_grade + num_parents_per_grade) * \
        (fifth_graders + sixth_graders + seventh_graders)

    # Calculate the number of buses needed
    num_buses = total_people // num_seats_per_bus
    if total_people % num_seats_per_bus != 0:
        num_buses += 1

    result = num_buses
    return result

print(solution())