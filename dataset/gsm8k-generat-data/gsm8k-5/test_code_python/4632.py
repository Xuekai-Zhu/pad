def solution():
    # Calculate the total cost of the meal, including the 20% tip
    total_cost = (10 + 20 + 30) * 1.2  # Tip is 20%, so total cost is 120% of the meal cost

    # Divide the total cost by the number of people to get the cost per person
    cost_per_person = total_cost / 3

    # Calculate the amount of tip each person should pay
    tip_per_person = cost_per_person * 0.2  # 20% of the cost per person is the tip

    result = tip_per_person
    return result

print(solution())