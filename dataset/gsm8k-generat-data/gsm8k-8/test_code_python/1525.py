def solution():
    # Calculate the number of students in the Biology class
    bio_class = 200 / 2

    # Determine the ratio of girls to boys in the Biology class
    girl_to_boy_ratio = 3/1

    # Calculate the total number of students in the Biology class
    bio_class_total = girl_to_boy_ratio + 1

    # Calculate the number of boys in the Biology class
    num_boys_bio_class = bio_class / bio_class_total

    result = num_boys_bio_class
    return result

print(solution())