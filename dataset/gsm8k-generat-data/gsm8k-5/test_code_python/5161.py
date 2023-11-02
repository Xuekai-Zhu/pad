def solution():
    # Convert gold coins to silver coins
    gold_to_silver = 3 * 60  # Each gold coin is worth 3 silver coins
    total_silver = gold_to_silver + 60  # Add the converted gold coins to the original silver coins

    # Convert silver coins to copper coins
    silver_to_copper = 8 * total_silver  # Each silver coin is worth 8 copper coins
    total_copper = silver_to_copper + 33  # Add the converted silver coins to the original copper coins

    result = total_copper
    return result

print(solution())