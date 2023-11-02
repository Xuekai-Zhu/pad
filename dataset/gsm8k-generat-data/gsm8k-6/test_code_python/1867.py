def solution():
    # Calculate the number of students who went to the playground
    playground_students = 20 - (20 / 4)  # 1/4 of the students stayed in the classroom

    # Calculate the number of boys on the playground
    boys = playground_students / 3  

    # Calculate the number of girls on the playground
    girls = playground_students - boys

    result = girls
    return result

print(solution())