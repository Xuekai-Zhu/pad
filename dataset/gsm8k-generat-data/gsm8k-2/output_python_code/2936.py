def solution():
    """The lunchroom is full of students: 40% are girls and the remainder are boys. There are 2 monitors for every 15 students. There are 8 monitors. Every boy drinks, on average, 1 carton of milk, and every girl drinks, on average, 2 cartons of milk. How many total cartons of milk are consumed by the students in the lunchroom?"""
    total_students = 100
    girls_percentage = 40
    boys_percentage = 100 - girls_percentage
    girls = (girls_percentage/100) * total_students
    boys = (boys_percentage/100) * total_students
    total_monitors = 8
    monitors_per_student = 2/15
    total_students_monitored = total_monitors/monitors_per_student
    total_cartons = (girls * 2) + (boys * 1)
    result = total_cartons
    return result

print(solution())