def solution():
    # Define the number of teachers for each child
    son_teachers = 3
    daughter_teachers = 4

    # Define the total amount spent on gifts
    total_spent = 70

    # Calculate the average cost of each gift
    average_gift_cost = total_spent / (son_teachers + daughter_teachers)
    result = average_gift_cost
    return result

print(solution())