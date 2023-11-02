def solution():
    # Define the number of students and chaperones
    num_students = 35
    num_chaperones = 4

    # Calculate the total cost for students and chaperones
    cost_students = num_students * 5
    cost_chaperones = num_chaperones * 6

    # Calculate the total entrance fee
    total_cost = cost_students + cost_chaperones
    result = total_cost
    return result

print(solution())