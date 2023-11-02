def solution():
    gift_money = 50
    novel_cost = 7
    lunch_cost = novel_cost * 2

    # Calculate the total cost of the novel and lunch
    total_cost = novel_cost + lunch_cost

    # Calculate the amount of money Jesse has left
    money_left = gift_money - total_cost
    result = money_left
    return result

print(solution())