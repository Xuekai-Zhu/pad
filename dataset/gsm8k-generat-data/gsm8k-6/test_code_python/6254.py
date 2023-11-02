def solution():
    # Calculate the total amount of money Geoffrey received
    total_received = 20 + 25 + 30  # €20 from grandmother, €25 from aunt and €30 from uncle

    # Calculate the total cost of the 3 video games
    total_cost = 3 * 35  # each game costs €35

    # Calculate how much money Geoffrey has left after buying the games
    remaining_money = 125 - total_received - total_cost

    result = remaining_money
    return result

print(solution())