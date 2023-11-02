def solution():
    total_money = 70  # Peter has $70 to spend on action figures for one day
    wooden_cost = 5  # Peter spends $5 on wooden action figures from Sunday to Wednesday
    plastic_cost = 2  # Peter spends $2 on plastic action figures for the rest of the week

    # Calculate the total cost of action figures for the week
    total_cost = (wooden_cost * 5) + (plastic_cost * 2)

    # Calculate the number of action figures Peter will have by the end of the week
    num_action_figures = total_cost / 7
    result = num_action_figures
    return result

print(solution())