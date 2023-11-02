def solution():
    # Define the cost of the first and second courses
    first_course_cost = 15
    second_course_cost = first_course_cost + 5

    # Calculate the cost of the dessert
    dessert_cost = 0.25 * second_course_cost

    # Calculate the total cost of the meal
    total_cost = first_course_cost + second_course_cost + dessert_cost

    # Calculate the amount of money Amelia will have left
    remaining_money = 60 - total_cost
    result = remaining_money
    return result

print(solution())