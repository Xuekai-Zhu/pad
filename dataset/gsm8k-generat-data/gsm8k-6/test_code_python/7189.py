def solution():
    # Find the total number of students in the class
    total_students = 11 + 13

    # Find the percentage of girls in the class before adding 1 boy
    girls_percentage = (13 / total_students) * 100

    # Find the percentage of girls in the class after adding 1 boy
    total_students += 1
    girls_percentage_new = (13 / total_students) * 100

    # Find the difference in percentage of girls before and after adding 1 boy
    difference = girls_percentage_new - girls_percentage

    result = difference
    return result

print(solution())