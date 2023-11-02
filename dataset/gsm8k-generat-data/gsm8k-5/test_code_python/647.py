def solution():
    cupcakes = 40  # Quinton brought 40 cupcakes to school
    cupcakes_given = (18 + 16 + 4)  # Quinton gave cupcakes to 18 students in Ms. Delmont's class, 16 students in Mrs. Donnelly's class, and 4 staff members
    cupcakes_left = cupcakes - cupcakes_given  # Calculate the number of cupcakes left over
    result = cupcakes_left
    return result

print(solution())