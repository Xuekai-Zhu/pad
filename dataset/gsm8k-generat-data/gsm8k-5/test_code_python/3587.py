def solution():
    total_students = 140  # There were 140 kids in the junior prom
    dancer_fraction = 1/4  # A fourth of the students were dancers
    dancer_students = total_students * dancer_fraction  # Calculate the number of dancer students
    slow_dancers = 25  # 25 students danced the slow dance

    # Calculate the number of dancer students who did not slow dance
    non_slow_dancers = dancer_students - slow_dancers
    result = non_slow_dancers
    return result

print(solution())