def solution():
    total_cost = 275 # 250 (gift) + 25 (cake)
    erika_savings = 155
    rick_savings = total_cost / 2

    # Calculate the total amount of money saved by Erika & Rick
    total_savings = erika_savings + rick_savings

    # Calculate the amount they will have left after buying the gift & cake
    left_money = total_savings - total_cost
    result = left_money
    return result

print(solution())