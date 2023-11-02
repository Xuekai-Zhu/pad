def solution():
    # Calculate the total number of people going to the museum
    total_people = 5  # Dorothy, her brother, her parents, and her grandfather

    # Calculate the cost of one regular ticket
    regular_ticket_cost = 10

    # Calculate the cost of one discounted ticket for people 18 years old or younger
    discounted_ticket_cost = regular_ticket_cost * 0.7

    # Calculate the total cost of the tickets for the group
    total_cost = (total_people - 1) * discounted_ticket_cost + regular_ticket_cost  # Dorothy is 15 years old and doesn't have a discount

    # Calculate the amount of money Dorothy will have after the trip
    initial_money = 70
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())