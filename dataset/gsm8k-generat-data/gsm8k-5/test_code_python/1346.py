def solution():
    spotted_brown_toads_per_acre = 50  # Given in the question
    brown_toads_per_acre = spotted_brown_toads_per_acre * 4  # There are 4 brown toads for every spotted brown toad
    green_toads_per_acre = brown_toads_per_acre / 25  # There are 25 brown toads for every green toad

    result = green_toads_per_acre
    return result

print(solution())