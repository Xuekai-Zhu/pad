def solution():
    num_friends = 6
    ticket_cost = 50
    entree_cost = 10
    drink_cost = 30
    num_drinkers = num_friends // 2

    # Calculate the total cost of tickets and entrees
    total_cost = num_friends * (ticket_cost + entree_cost)

    # If half the group bought drink tickets, add that cost
    if num_drinkers > 0:
        total_cost += num_drinkers * drink_cost

    # Calculate the refund amount
    refund_amount = 0.9 * total_cost

    # Calculate the amount lost by the group
    loss_amount = total_cost - refund_amount
    result = loss_amount
    return result

print(solution())