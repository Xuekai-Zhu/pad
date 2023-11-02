def solution():
    # Calculate the number of people in Dorothy's family
    num_people = 1 + 1 + 2 + 1  # Dorothy + brother + parents + grandfather

    # Calculate the number of people in Dorothy's family who are 18 or younger
    num_discounted = 1 + 1  # Dorothy + brother are 18 or younger

    # Calculate the cost of tickets for Dorothy's family
    cost_per_ticket = 10
    cost_before_discount = num_people * cost_per_ticket
    cost_after_discount = cost_before_discount - (num_discounted * 0.3 * cost_per_ticket)

    # Calculate how much money Dorothy will have after the trip
    starting_money = 70
    money_left = starting_money - cost_after_discount
    result = money_left
    return result

print(solution())