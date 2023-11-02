def solution():
    # Calculate the number of water balloons Randy has
    randy_balloons = 6 * 2  # Janice has 6 water balloons and Randy has half as many as Janice

    # Calculate the number of water balloons Cynthia has
    cynthia_balloons = randy_balloons * 4  # Cynthia has four times as many water balloons as Randy

    result = cynthia_balloons
    return result

print(solution())