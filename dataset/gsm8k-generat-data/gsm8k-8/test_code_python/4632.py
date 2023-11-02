def solution():
    # Calculate the total cost of the meal
    total_cost = 10 + 20 + 30

    # Calculate the total amount of the tip
    total_tip = total_cost * 0.2

    # Calculate the amount each person should pay for the tip
    tip_per_person = total_tip / 3

    result = tip_per_person
    return result

print(solution())