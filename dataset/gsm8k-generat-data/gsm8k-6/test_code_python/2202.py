def solution():
    # Calculate the total amount of ink used in one day
    ink_per_board = 20  # ml of ink needed for one whiteboard per day
    total_ink = 5 * 2 * ink_per_board  # 5 classes, each using 2 whiteboards
    cost_per_ml = 0.5  # cost of ink is 50 cents per ml
    total_cost = total_ink * cost_per_ml  # calculate the total cost in dollars

    result = total_cost
    return result

print(solution())