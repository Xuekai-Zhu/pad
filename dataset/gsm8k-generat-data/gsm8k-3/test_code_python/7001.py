def solution():
    """Andrew bought a big bag of balloons. The bag had 303 blue balloons and 453 purple balloons. If Andrew shares half of his balloons with his brother, how many balloons does he have left?"""
    # Calculate the total number of balloons in the bag
    total_balloons = 303 + 453

    # Calculate the number of balloons Andrew shares with his brother
    shared_balloons = total_balloons / 2

    # Calculate the number of balloons Andrew has left
    remaining_balloons = total_balloons - shared_balloons

    # Display the number of balloons Andrew has left
    result = remaining_balloons
    return result

print(solution())