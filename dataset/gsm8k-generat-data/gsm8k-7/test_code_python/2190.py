def solution():
    num_friends = 6
    ticket_price = 50
    entree_price = 10
    drink_price = 30
    num_drinkers = num_friends // 2
    refund_rate = 0.9

    # Calculate the total cost for tickets and entrees
    total_cost = (ticket_price + entree_price) * num_friends

    # Calculate the total cost for drinks
    total_drinks_cost = drink_price * num_drinkers

    # Calculate the total amount paid by the group
    total_paid = total_cost + total_drinks_cost

    # Calculate the total refund for the group
    total_refund = total_paid * refund_rate

    # Calculate how much money the group lost
    money_lost = total_paid - total_refund
    result = money_lost
    return result

print(solution())