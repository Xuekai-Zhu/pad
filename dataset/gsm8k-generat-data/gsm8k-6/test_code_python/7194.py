def solution():
    # Calculate the distance Sarah swims per day
    distance_julien = 50  # Julien swims 50 meters per day
    distance_sarah = distance_julien / 2  # Sarah swims twice the distance of Julien
    distance_jamir = distance_sarah + 20  # Jamir swims 20 more meters per day than Sarah

    # Calculate the total distance all three of them swam in a week
    total_distance = (distance_julien + distance_sarah + distance_jamir) * 7  # they swim the same distance every day for a week

    result = total_distance
    return result

print(solution())