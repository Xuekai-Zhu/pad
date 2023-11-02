def solution():
    # Find the total weight of Chicken Surprise
    total_weight = 4.5 + (24/16)  # convert 24 ounces to pounds

    # Find the weight of one serving of Chicken Surprise
    weight_per_serving = total_weight / 12

    # Convert the weight of one serving to ounces
    weight_per_serving_oz = weight_per_serving * 16

    result = weight_per_serving_oz
    return result

print(solution())