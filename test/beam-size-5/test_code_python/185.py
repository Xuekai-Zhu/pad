def solution():
    num_friends = 3
    ticket_price = 20.25
    food_price = ticket_price - 4.5
    ride_price = 33
    num_rides = 2

    # Calculate the total cost of all tickets
    total_tickets_cost = num_friends * ticket_price

    # Calculate the total cost of all food
    total_food_cost = num_food_cost * food_price

    # Calculate the total cost of all rides
    total_rides_cost = num_rides * ride_price

    # Calculate the total cost of all friends
    total_cost = total_tickets_cost + total_food_cost + total_rides_cost

    # Calculate the cost per person
    cost_per_person = total_cost / num_friends
    result = cost_per_person
    return result

print(solution())