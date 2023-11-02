def solution():
    """Peter knows that the distance an airplane travels between Spain and Russia is 7019 km, while the distance between Spain and Germany is 1615 km. Peter took a flight from Spain, which made a stopover in Germany, while being there, he receives a call from his brother asking him how many kilometers he has to fly to get to Russia and then return to Spain. What will Peter answer?"""
    spain_to_germany = 1615
    spain_to_russia = 7019

    # distance from Germany to Russia and back to Spain
    germany_to_russia_to_spain = (spain_to_germany + spain_to_russia) * 2

    result = germany_to_russia_to_spain
    return result

print(solution())