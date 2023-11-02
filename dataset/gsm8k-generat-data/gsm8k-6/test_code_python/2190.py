def solution():
    num_friends = 6
    ticket_cost = 50
    entree_cost = 10
    drink_cost = 30

    # Calculate the total cost without drinks
    total_cost = num_friends * (ticket_cost + entree_cost)

    # Calculate the number of friends buying drinks
    num_drinkers = num_friends // 2

    # Add the cost of drinks for those who bought them
    total_cost += num_drinkers * drink_cost

    # Calculate the refund amount
    refund_amount = 0.9 * total_cost

    # Calculate how much money the group lost
    lost_money = total_cost - refund_amount
    result = lost_money
    return result

print(solution())