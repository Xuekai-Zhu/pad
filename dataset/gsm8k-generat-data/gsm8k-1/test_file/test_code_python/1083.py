def solution():
    """A farmer is baling hay in their field. Each hour the farmer makes 5 bales. At the same time, a truck is picking the hay bales up. Each hour the truck picks up 3 bales of hay. If the farmer and the truck driver put in a 6 hour day, how many bales of hay are left in the field?"""
    bales_per_hour_farm = 5
    bales_per_hour_truck = 3
    hours_worked = 6
    total_bales = bales_per_hour_farm * hours_worked
    total_pickup = bales_per_hour_truck * hours_worked
    bales_left = total_bales - total_pickup
    result = bales_left
    return result

print(solution())