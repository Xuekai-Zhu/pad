def solution():
    """There are 30 spaces for each vehicle in a parking lot. A caravan takes up a total of 2 spaces of parking space. How many vehicles can still park if there are 3 caravans currently parking?"""
    total_parking_spaces = 30
    caravan_spaces = 2
    remaining_spaces = total_parking_spaces - caravan_spaces
    cars_parked = remaining_spaces // total_parking_spaces
    cars_left = cars_parked - 3
    result = cars_left
    return result

print(solution())