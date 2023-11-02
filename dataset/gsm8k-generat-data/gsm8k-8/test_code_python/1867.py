def solution():
    # Find the number of students who went to the playground
    playground_students = 20 - (20 * 0.25)

    # Find the number of boys on the playground
    boys_on_playground = playground_students * (1/3)

    # Find the number of girls on the playground
    girls_on_playground = playground_students - boys_on_playground

    result = girls_on_playground
    return result

print(solution())