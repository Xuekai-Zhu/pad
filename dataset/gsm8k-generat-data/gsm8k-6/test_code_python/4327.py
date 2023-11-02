def solution():
    # Calculate the amount of money Samuel spent on food
    samuel_food = 6

    # Calculate the amount of money Kevin spent on his ticket
    kevin_ticket = 20 - samuel_food - 14 - 2

    # Calculate the amount of money Kevin spent on food
    kevin_food = 20 - samuel_food - kevin_ticket - 14 - 2

    result = kevin_food
    return result

print(solution())