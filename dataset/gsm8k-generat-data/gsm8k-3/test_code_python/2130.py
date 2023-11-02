def solution():
    """Amelia has $60 to spend on her dinner at a restaurant. The first course costs $15 and the second course $5 more. The cost of the dessert is 25% of the price of the second course. How much money will Amelia have left after buying all those meals?"""
    # Define the cost of the first course and the increase in cost for the second course
    first_course_cost = 15
    second_course_additional_cost = 5

    # Calculate the cost of the second course
    second_course_cost = first_course_cost + second_course_additional_cost

    # Calculate the cost of the dessert
    dessert_cost = 0.25 * second_course_cost

    # Calculate the total cost of Amelia's dinner
    total_cost = first_course_cost + second_course_cost + dessert_cost

    # Calculate the money Amelia will have left after buying all those meals
    money_left = 60 - total_cost

    # Display the money left
    result = money_left
    return result

print(solution())