def solution():
    # Define the cost of one bow, one bottle of vinegar, and one box of baking soda
    bow_cost = 5
    vinegar_cost = 2
    baking_soda_cost = 1

    # Calculate the total cost of supplies for one student
    student_cost = bow_cost + vinegar_cost + baking_soda_cost

    # Calculate the total cost of supplies for the class
    class_cost = student_cost * 23
    result = class_cost
    return result

print(solution())