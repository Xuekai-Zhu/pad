def solution():
    """The lunchroom is full of students: 40% are girls and the remainder are boys. There are 2 monitors for every 15 students. There are 8 monitors. Every boy drinks, on average, 1 carton of milk, and every girl drinks, on average, 2 cartons of milk. How many total cartons of milk are consumed by the students in the lunchroom?"""
    # Define the total number of students
    total_students = 100

    # Calculate the number of girls and boys
    girls = total_students * 0.4
    boys = total_students - girls

    # Calculate the number of monitors
    monitors = 8

    # Calculate the number of students per monitor
    students_per_monitor = 15 / 2

    # Calculate the total number of cartons of milk consumed by boys
    boy_milk = boys * 1

    # Calculate the total number of cartons of milk consumed by girls
    girl_milk = girls * 2

    # Calculate the total number of cartons of milk consumed by all students
    total_milk = boy_milk + girl_milk

    # return the result
    result = total_milk
    return result

print(solution())