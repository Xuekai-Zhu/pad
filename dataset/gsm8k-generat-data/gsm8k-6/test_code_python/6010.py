def solution():
    # Calculate the weight James can carry for 20 meters without straps
    weight_20_meters = 300

    # Calculate the weight James can carry for 10 meters without straps
    weight_10_meters = weight_20_meters * 1.3

    # Calculate the weight James can carry for 10 meters with lifting straps
    weight_with_straps = weight_10_meters * 1.2

    # Increase the 20-meter weight by 50 pounds and adjust the other weights proportionally
    weight_20_meters += 50
    weight_10_meters = weight_20_meters * 1.3
    weight_with_straps = weight_10_meters * 1.2

    result = weight_with_straps
    return result

print(solution())