def solution():
    num_friends = 3
    ticket_price = 7
    num_popcorn_boxes = 2
    popcorn_price = 1.5
    num_milk_tea_cups = 3
    milk_tea_price = 3

    # Calculate the total cost of all tickets
    total_tickets_cost = num_friends * ticket_price

    # Calculate the total cost of all popcorn boxes
    total_popcorn_cost = num_popcorn_boxes * popcorn_price

    # Calculate the total cost of all cups of milk tea
    total_milk_tea_cost = num_milk_tea_cups * milk_tea_price

    # Calculate the total cost of all expenses
    total_cost = total_tickets_cost + total_popcorn_cost + total_milk_tea_cost

    # Calculate the amount each friend should contribute
    contribution = total_cost / num_friends
    result = contribution
    return result

print(solution())