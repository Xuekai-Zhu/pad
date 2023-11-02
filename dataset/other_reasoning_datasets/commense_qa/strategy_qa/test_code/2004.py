def solution():
    sea_world_locations = ["San Diego", "Orlando", "San Antonio"]
    shamu_location = "San Diego"
    if shamu_location in sea_world_locations:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())