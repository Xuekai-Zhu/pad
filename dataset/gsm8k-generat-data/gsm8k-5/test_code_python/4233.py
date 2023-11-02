def solution():
    potatoes_per_person = 1.5  # Each person eats 1.5 pounds of potatoes
    num_people = 40  # James is making potatoes for 40 people
    total_potatoes = potatoes_per_person * num_people  # James needs to make this many pounds of potatoes
    cost_per_pound = 5 / 20  # A 20-pound bag of potatoes costs $5
    total_cost = total_potatoes * cost_per_pound  # James needs to spend this much on potatoes
    result = total_cost
    return result

print(solution())