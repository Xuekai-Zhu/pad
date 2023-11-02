def solution():
    num_students = 23
    bow_cost = 5
    vinegar_cost = 2
    baking_soda_cost = 1

    # Calculate the total cost of bows for all students
    total_bow_cost = num_students * bow_cost

    # Calculate the total cost of bottles of vinegar for all students
    total_vinegar_cost = num_students * vinegar_cost

    # Calculate the total cost of boxes of baking soda for all students
    total_baking_soda_cost = num_students * baking_soda_cost

    # Calculate the total cost of all supplies
    total_cost = total_bow_cost + total_vinegar_cost + total_baking_soda_cost
    result = total_cost
    return result

print(solution())