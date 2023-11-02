def solution():
    num_giant_roaches = 12
    num_scorpions = 3
    num_crickets = num_giant_roaches / 2
    num_caterpillars = num_scorpions * 2

    # Calculate the total number of insects in Calvin's collection
    total_insects = num_giant_roaches + num_scorpions + num_crickets + num_caterpillars
    result = total_insects
    return result

print(solution())