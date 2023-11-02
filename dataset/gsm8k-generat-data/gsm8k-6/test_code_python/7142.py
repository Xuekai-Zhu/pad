def solution():
    cheapest_lamp = 20  # cost of the cheapest lamp
    expensive_lamp = 3 * cheapest_lamp  # cost of the most expensive lamp
    frank_money = 90  # Frank's current amount of money
    remaining_money = frank_money - expensive_lamp  # Frank's money remaining after buying the most expensive lamp
    result = remaining_money
    return result

print(solution())