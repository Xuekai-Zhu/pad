def solution():
    physics_class = 200
    bio_class = physics_class / 2  # Biology class has half as many students as Physics class
    num_girls = 3 * num_boys  # There are three times as many girls as boys in the Biology class

    # Total number of students in Biology class
    total_students = num_boys + num_girls

    # Total number of boys in the Biology class
    num_boys_bio = (total_students / 4)  # Boys make up one-fourth of the class in total
    result = num_boys_bio
    return result

print(solution())