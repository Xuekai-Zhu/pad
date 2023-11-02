def solution():
    # Define the terms and their relationship
    game_engine = "software"
    fuel_injector = "part"
    automotive_engine = "vehicle"
    # Check if a game engine has a fuel injector
    if fuel_injector not in game_engine:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())