def solution():
    # Define Jesse's initial gift amount and the cost of the novel
    initial_gift = 50
    novel_cost = 7

    # Calculate the cost of her lunch, which is twice the cost of the novel
    lunch_cost = 2 * novel_cost

    # Calculate the total cost of her purchases
    total_cost = novel_cost + lunch_cost

    # Calculate how much money Jesse has left after her purchases
    remaining_money = initial_gift - total_cost
    result = remaining_money
    return result

print(solution())