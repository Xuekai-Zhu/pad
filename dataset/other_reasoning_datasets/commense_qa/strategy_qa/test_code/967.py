def solution():
    caracal_leap_height = 12.0
    javier_sotomayor_jump_height = 2.45 # in meters
    # Convert caracal leap height to meters
    caracal_leap_height_meters = caracal_leap_height / 3.2808
    if caracal_leap_height_meters > javier_sotomayor_jump_height:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())