def solution():
    """Micah drank 1.5 liters of water in the morning. Then she drank three times that much water in the afternoon. How many liters of water did she drink from the morning until the afternoon?"""
    # Define the amount of water Micah drank in the morning
    morning_drink = 1.5

    # Define the amount of water Micah drank in the afternoon
    afternoon_drink = morning_drink * 3

    # Calculate the total amount of water Micah drank from morning until afternoon
    total_drink = morning_drink + afternoon_drink

    result = total_drink
    return result

print(solution())