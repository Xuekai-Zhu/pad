def solution():
    brown_spotted_toads_per_acre = 50
    brown_toads_per_green_toad = 25

    # Calculate the total number of brown toads per acre (spotted and unspotted)
    total_brown_toads_per_acre = brown_spotted_toads_per_acre * 4

    # Calculate the total number of green toads per acre
    total_green_toads_per_acre = total_brown_toads_per_acre / brown_toads_per_green_toad

    result = total_green_toads_per_acre
    return result

print(solution())