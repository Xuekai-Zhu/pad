def solution():
    """Amelia has $60 to spend on her dinner at a restaurant. The first course costs $15 and the second course $5 more. The cost of the dessert is 25% of the price of the second course. How much money will Amelia have left after buying all those meals?"""
    total_money = 60
    first_course_cost = 15
    second_course_cost = 20
    dessert_cost = 0.25 * second_course_cost
    total_cost = first_course_cost + second_course_cost + dessert_cost
    remaining_money = total_money - total_cost
    result = remaining_money
    return result

print(solution())