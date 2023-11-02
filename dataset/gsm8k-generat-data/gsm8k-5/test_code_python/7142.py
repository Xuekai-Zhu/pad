def solution():
    cheapest_lamp = 20  # The cost of the cheapest lamp is $20
    most_expensive_lamp = 3 * cheapest_lamp  # The most expensive lamp is 3 times more expensive
    available_money = 90  # Frank currently has $90

    # Calculate the amount of money Frank will have remaining after buying the most expensive lamp
    remaining_money = available_money - most_expensive_lamp
    result = remaining_money
    return result

print(solution())