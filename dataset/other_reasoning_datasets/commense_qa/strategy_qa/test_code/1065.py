def solution():
    eiffel_tower_height = 984
    eiffel_tower_visitor_platform_height = 906
    empire_state_building_height = 1230
    if empire_state_building_height > (eiffel_tower_height + eiffel_tower_visitor_platform_height):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())