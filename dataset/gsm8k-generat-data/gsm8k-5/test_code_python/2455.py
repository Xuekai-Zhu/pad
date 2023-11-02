def solution():
    num_students = 23  # There are 23 students in the class
    cost_bow = 5  # Each bow costs $5
    cost_vinegar = 2  # Each bottle of vinegar costs $2
    cost_baking_soda = 1  # Each box of baking soda costs $1

    # Calculate the total cost of supplies for all students
    total_cost = num_students * (cost_bow + cost_vinegar + cost_baking_soda)

    result = total_cost
    return result

print(solution())