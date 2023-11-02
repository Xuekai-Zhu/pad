def solution():
    num_people = 6
    meat_per_person = 0.5  # in pounds
    cost_per_pound = 15.0

    # Calculate the total amount of meat needed
    total_meat = num_people * meat_per_person

    # Calculate the total cost of the meat needed
    total_cost = total_meat * cost_per_pound
    result = total_cost
    return result

print(solution())