def solution():
    # Calculate the total number of cupcakes Dani brings
    cupcakes = 2.5 * 12

    # Calculate the total number of people in the class
    total_people = 27 + 1 + 1  # students + teacher + teacher's aide

    # Subtract the sick students from the total number of people
    total_people -= 3

    # Subtract the cupcakes given to each person in the class
    cupcakes -= total_people

    result = cupcakes
    return result

print(solution())