def solution():
    """Three friends spent $20.25 on 3 tickets to the fair. They also spent $4.50 less on food than on the tickets. They also went on 2 different rides which costs $33 for each ride. If they agreed to split all the costs evenly, how much did each of them pay?"""
    ticket_price = 20.25 / 3
    food_price = ticket_price - 4.5
    ride_price = 33 * 2
    total_cost = 20.25 + food_price * 3 + ride_price
    cost_per_person = total_cost / 3
    result = cost_per_person
    return result

print(solution())