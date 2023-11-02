def solution():
    """Derek is watching the construction cranes downtown and is trying to figure out how much taller they have to be than the building they are building. He sees one crane that is 228 feet tall finishing a building that was 200 feet tall. He sees another that is 120 feet tall finishing a building that is 100 feet tall. The final crane he sees is 147 feet tall, finishing a building that is 140 feet tall. On average, what percentage taller are the cranes than the building?"""
    crane_heights = [228, 120, 147]
    building_heights = [200, 100, 140]
    differences = [crane_heights[i] - building_heights[i] for i in range(3)]
    avg_difference = sum(differences) / len(differences)
    avg_percent_taller = (avg_difference / sum(building_heights)) * 100
    result = avg_percent_taller
    return result

print(solution())