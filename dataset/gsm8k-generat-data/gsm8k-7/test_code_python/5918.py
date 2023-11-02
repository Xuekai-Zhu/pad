def solution():
    rise_rate = 50
    descend_rate = -10

    # Calculate the elevation gained during the first 15 minutes
    elevation_gain_1 = rise_rate * 15

    # Calculate the elevation lost during the next 10 minutes
    elevation_loss = descend_rate * 10

    # Calculate the elevation gained during the next 15 minutes
    elevation_gain_2 = rise_rate * 15

    # Calculate the total elevation gain
    total_gain = elevation_gain_1 + elevation_gain_2

    # Calculate the highest elevation reached by the balloon
    highest_elevation = total_gain + elevation_loss
    result = highest_elevation
    return result

print(solution())