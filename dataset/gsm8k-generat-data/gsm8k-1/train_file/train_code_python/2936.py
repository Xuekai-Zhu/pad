def solution():
    """The lunchroom is full of students: 40% are girls and the remainder are boys. There are 2 monitors for every 15 students. There are 8 monitors. Every boy drinks, on average, 1 carton of milk, and every girl drinks, on average, 2 cartons of milk. How many total cartons of milk are consumed by the students in the lunchroom?"""
    total_students = 100  # assume there are 100 students for ease of calculation
    girls_percent = 40
    boys_percent = 100 - girls_percent
    girls_count = total_students * girls_percent / 100
    boys_count = total_students * boys_percent / 100
    total_monitors = 8
    monitors_per_student = 2/15
    total_cartons = (girls_count * 2) + (boys_count * 1)
    result = total_cartons
    return result

print(solution())