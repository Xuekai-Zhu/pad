def solution():
    """James makes potatoes for a group. Each person eats 1.5 pounds of potatoes. He makes potatoes for 40 people. A 20-pound bag of potatoes costs $5. How much does it cost?"""
    potatoes_per_person = 1.5
    number_of_people = 40
    pounds_of_potatoes = potatoes_per_person * number_of_people
    bags_of_potatoes = pounds_of_potatoes / 20
    cost_per_bag = 5
    total_cost = bags_of_potatoes * cost_per_bag
    result = total_cost
    return result

print(solution())