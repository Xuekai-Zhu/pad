def solution():
    # Calculate the total cost of the sheet, rope, and propane tank
    total_cost = 42 + 18 + 14

    # Calculate the amount of money they have left
    money_left = 200 - total_cost

    # Calculate the maximum amount of helium they can buy with the money they have left
    max_helium = money_left / 1.5

    # Calculate the maximum height they can fly the balloon
    max_height = max_helium * 113
    result = max_height
    return result

print(solution())