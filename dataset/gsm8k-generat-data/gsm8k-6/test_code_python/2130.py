def solution():
    # Calculate the cost of the second course and the dessert
    second_course_cost = 15 + 5  # the second course costs $5 more than the first
    dessert_cost = 0.25 * second_course_cost  # the dessert costs 25% of the price of the second course

    # Calculate the total cost of Amelia's meal
    total_cost = 15 + second_course_cost + dessert_cost

    # Calculate the amount of money Amelia will have left after buying all those meals
    money_left = 60 - total_cost
    result = money_left
    return result

print(solution())