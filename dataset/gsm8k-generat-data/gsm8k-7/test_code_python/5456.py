def solution():
    total_students = 100
    boy_ratio = 3
    girl_ratio = 2

    # Calculate the total number of parts in the ratio
    total_parts = boy_ratio + girl_ratio

    # Calculate the number of parts that represent the girls
    girl_parts = total_students / total_parts * girl_ratio

    # Calculate the number of parts that represent the boys
    boy_parts = total_students / total_parts * boy_ratio

    # Calculate the difference between the number of boys and girls
    difference = boy_parts - girl_parts
    result = difference
    return result

print(solution())