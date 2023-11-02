def solution():
    total_students = 100 # Assume a total of 100 students for easier calculation
    girls = 40 # 40% of the students are girls
    boys = 100 - girls # The remainder are boys
    monitors = 8 # There are 8 monitors
    students_per_monitor = 15 # There are 2 monitors for every 15 students
    total_cartons = (girls * 2) + (boys * 1) # Total cartons of milk consumed by students

    # Calculate the total number of students being monitored
    total_monitored_students = monitors * students_per_monitor

    # Calculate the total cartons of milk per monitored student
    cartons_per_student = total_cartons / total_students

    # Calculate the total cartons of milk consumed by all monitored students
    total_monitored_cartons = cartons_per_student * total_monitored_students

    result = total_monitored_cartons
    return result

print(solution())