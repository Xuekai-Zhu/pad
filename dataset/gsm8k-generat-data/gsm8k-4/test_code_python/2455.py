def solution():
    """A teacher has to order supplies for his class to do a science project. Each student needs a bow, a small bottle of vinegar and a box of baking soda. Bows are $5 each, a bottle of vinegar is $2 and a box of baking soda is $1. The teacher has 23 students in this class. How much will the supplies cost?"""
    # Define the prices of bows, vinegar and baking soda
    bow_price = 5
    vinegar_price = 2
    baking_soda_price = 1

    # Define the number of students
    students = 23

    # Calculate the total cost of supplies
    total_cost = (bow_price + vinegar_price + baking_soda_price) * students

    result = total_cost
    return result

print(solution())