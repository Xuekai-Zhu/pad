def solution():
    # Define the cost of one candy bar and one bag of chips
    candy_bar_cost = 2
    chip_cost = 0.5

    # Calculate the total cost for one student
    total_cost_per_student = (1 * candy_bar_cost) + (2 * chip_cost)

    # Calculate the total cost for 5 students
    total_cost_for_5_students = total_cost_per_student * 5

    result = total_cost_for_5_students
    return result

print(solution())