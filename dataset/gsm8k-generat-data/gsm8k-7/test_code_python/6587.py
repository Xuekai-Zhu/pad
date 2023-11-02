def solution():
    num_students = 100
    num_girls = num_students / 2
    num_boys = num_students / 2
    girl_dog_percentage = 0.20
    boy_dog_percentage = 0.10

    # Calculate the number of girls who have dogs
    num_girl_dog_owners = num_girls * girl_dog_percentage

    # Calculate the number of boys who have dogs
    num_boy_dog_owners = num_boys * boy_dog_percentage

    # Calculate the total number of students who have dogs
    total_dog_owners = num_girl_dog_owners + num_boy_dog_owners
    result = total_dog_owners
    return result

print(solution())