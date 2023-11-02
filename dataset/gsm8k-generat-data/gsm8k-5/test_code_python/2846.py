def solution():
    game_cost = 60  # The video game costs $60
    candy_cost = 5  # The candy costs $5
    total_cost = game_cost + candy_cost  # The total cost of the purchases
    hours_worked = 9  # Chris works 9 hours
    hourly_rate = 8  # Chris earns $8 per hour
    earnings = hours_worked * hourly_rate  # Chris earns $8 for every hour he babysits
    leftover_money = earnings - total_cost  # Calculate the money left over after making the purchases

    result = leftover_money
    return result

print(solution())