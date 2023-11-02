def solution():
    num_people = 10
    chips_per_person = 1.2
    cost_per_pound = 0.25

    # Calculate the total amount of chips needed for the party
    total_chips = num_people * chips_per_person

    # Calculate the total cost of the chips
    total_cost = total_chips * cost_per_pound
    result = total_cost
    return result

print(solution())