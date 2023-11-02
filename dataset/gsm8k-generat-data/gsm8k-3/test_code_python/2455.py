def solution():
    """A teacher has to order supplies for his class to do a science project. Each student needs a bow, a small bottle of vinegar and a box of baking soda. Bows are $5 each, a bottle of vinegar is $2 and a box of baking soda is $1. The teacher has 23 students in this class. How much will the supplies cost?"""
    # Define the cost of each supply
    BOW_COST = 5
    VINEGAR_COST = 2
    BAKING_SODA_COST = 1

    # Define the number of students
    students = 23

    # Calculate the total cost of bows
    bow_cost = students * BOW_COST

    # Calculate the total cost of vinegar
    vinegar_cost = students * VINEGAR_COST

    # Calculate the total cost of baking soda
    baking_soda_cost = students * BAKING_SODA_COST

    # Calculate the total cost of all supplies
    total_cost = bow_cost + vinegar_cost + baking_soda_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())