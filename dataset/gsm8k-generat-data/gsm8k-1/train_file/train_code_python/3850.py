def solution():
    """Peter knows that the distance an airplane travels between Spain and Russia is 7019 km, while the distance between Spain and Germany is 1615 km. Peter took a flight from Spain, which made a stopover in Germany, while being there, he receives a call from his brother asking him how many kilometers he has to fly to get to Russia and then return to Spain. What will Peter answer?"""
    spain_to_germany = 1615
    spain_to_russia = 7019
    round_trip_distance = (spain_to_germany*2) + (spain_to_russia*2)
    result = round_trip_distance
    return result

print(solution())