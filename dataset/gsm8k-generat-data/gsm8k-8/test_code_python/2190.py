def solution():
    # Define the number of people and costs
    num_people = 6
    ticket_cost = 50
    entree_cost = 10
    drink_cost = 30
    num_drinkers = num_people // 2

    # Calculate the total cost before refund
    total_cost = num_people * (ticket_cost + entree_cost)
    total_cost += num_drinkers * drink_cost

    # Calculate the refund amount and total lost money
    refund_amount = total_cost * 0.9
    lost_money = total_cost - refund_amount
    result = lost_money
    return result

print(solution())