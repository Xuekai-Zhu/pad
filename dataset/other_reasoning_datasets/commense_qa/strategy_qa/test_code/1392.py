def solution():
    brazilian_navy_ship_types = ["guided missile frigates"]
    british_made_ships = ["guided missile frigates"]
    if any(ship_type in british_made_ships for ship_type in brazilian_navy_ship_types):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())