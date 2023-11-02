def solution():
    # Calculate the total amount of money Erika and her brother have
    total_money = 155 + (250/2)  # Erika saved $155 and her brother saved half of the cost of the gift

    # Calculate the total cost of the gift and cake
    total_cost = 250 + 25  # gift costs $250 and cake costs $25

    # Calculate the amount of money leftover after buying the gift and cake
    money_leftover = total_money - total_cost
    result = money_leftover
    return result

print(solution())