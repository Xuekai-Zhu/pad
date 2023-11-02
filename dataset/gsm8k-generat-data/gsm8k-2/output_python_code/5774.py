def solution():
    """There are 30 spaces for each vehicle in a parking lot. A caravan takes up a total of 2 spaces of parking space. How many vehicles can still park if there are 3 caravans currently parking?"""
    total_spaces = 30
    caravan_spaces = 2
    remaining_spaces = total_spaces - caravan_spaces
    vehicles_per_space = 1
    parked_vehicles = 3 * (caravan_spaces // 2)
    available_spaces = (remaining_spaces * vehicles_per_space) - parked_vehicles
    result = available_spaces
    return result

print(solution())