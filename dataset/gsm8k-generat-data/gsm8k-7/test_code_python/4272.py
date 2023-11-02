def solution():
    num_servings = 12
    chicken_weight = 4.5  # pounds
    stuffing_weight = 24  # ounces

    # Calculate the total weight of Chicken Surprise
    total_weight = chicken_weight + (stuffing_weight / 16)  # convert stuffing to pounds

    # Calculate the weight of one serving of Chicken Surprise
    serving_weight = total_weight / num_servings

    # Convert the serving weight to ounces
    serving_weight_oz = serving_weight * 16

    result = serving_weight_oz
    return result

print(solution())