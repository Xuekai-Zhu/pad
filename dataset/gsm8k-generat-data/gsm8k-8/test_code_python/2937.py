def solution():
    # Calculate the number of students
    total_students = 100

    # Calculate the number of girls
    girls = 0.4 * total_students

    # Calculate the number of boys
    boys = total_students - girls

    # Calculate the number of monitors
    monitors = 8

    # Calculate the number of students per monitor
    students_per_monitor = 15 / 2

    # Calculate the total number of milk cartons
    boy_cartons = boys * 1
    girl_cartons = girls * 2
    total_cartons = boy_cartons + girl_cartons

    # Calculate the total number of milk cartons per monitor
    cartons_per_monitor = total_cartons / (total_students / students_per_monitor)

    result = cartons_per_monitor * monitors
    return result

print(solution())