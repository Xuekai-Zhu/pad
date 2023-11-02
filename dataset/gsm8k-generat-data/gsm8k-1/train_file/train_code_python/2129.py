def solution():
    """Amelia has $60 to spend on her dinner at a restaurant. The first course costs $15 and the second course $5 more. The cost of the dessert is 25% of the price of the second course. How much money will Amelia have left after buying all those meals?"""
    total_budget = 60
    first_course = 15
    second_course = first_course + 5
    dessert = 0.25 * second_course
    total_spent = first_course + second_course + dessert
    money_left = total_budget - total_spent
    result = money_left
    return result

print(solution())