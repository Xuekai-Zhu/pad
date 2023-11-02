def solution():
    num_friends = 5
    normal_price = 50
    scalper_multiplier = 2.4
    scalper_discount = 10
    friend_discount = 0.6

    # Calculate the total cost of the two normal priced tickets
    normal_tickets_cost = 2 * normal_price

    # Calculate the cost of the two scalper tickets
    scalper_tickets_cost = 2 * normal_price * scalper_multiplier - scalper_discount

    # Calculate the cost of the friend's discounted ticket
    friend_ticket_cost = normal_price * friend_discount

    # Calculate the total cost of all the tickets
    total_cost = normal_tickets_cost + scalper_tickets_cost + friend_ticket_cost

    # Divide the total cost by the number of friends to find the cost per person
    cost_per_person = total_cost / num_friends
    result = cost_per_person
    return result

print(solution())