def solution():
    """Peter knows that the distance an airplane travels between Spain and Russia is 7019 km, while the distance between Spain and Germany is 1615 km. Peter took a flight from Spain, which made a stopover in Germany, while being there, he receives a call from his brother asking him how many kilometers he has to fly to get to Russia and then return to Spain. What will Peter answer?"""
    # Define the distance of the trip from Spain to Germany and back to Spain
    round_trip_distance = 2 * 1615

    # Define the distance of the trip from Spain to Russia and back to Spain
    round_trip_distance += 2 * 7019

    # Calculate the total distance of the trip
    total_distance = round_trip_distance

    # Return Peter's answer to his brother
    result = total_distance
    return result

print(solution())