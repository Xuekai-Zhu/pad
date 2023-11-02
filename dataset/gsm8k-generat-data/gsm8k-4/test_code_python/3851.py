def solution():
    """Peter knows that the distance an airplane travels between Spain and Russia is 7019 km, while the distance between Spain and Germany is 1615 km. Peter took a flight from Spain, which made a stopover in Germany, while being there, he receives a call from his brother asking him how many kilometers he has to fly to get to Russia and then return to Spain. What will Peter answer?"""
    # Define the distances
    spain_germany = 1615
    spain_russia = 7019

    # Calculate the total distance Peter would have to fly
    total_distance = spain_germany + spain_russia + spain_germany

    # Return the result
    result = total_distance
    return result

print(solution())