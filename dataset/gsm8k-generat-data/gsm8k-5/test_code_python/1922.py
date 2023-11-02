def solution():
    cars_money = 3 * 10  # Stormi earns $30 from washing cars
    lawns_money = 2 * 13  # Stormi earns $26 from mowing lawns
    total_money = cars_money + lawns_money  # Stormi earned a total of $56
    bike_cost = 80  # The bicycle Stormi wants to buy costs $80

    # Calculate how much more money Stormi needs to afford the bicycle
    remaining_money = bike_cost - total_money
    result = remaining_money
    return result

print(solution())