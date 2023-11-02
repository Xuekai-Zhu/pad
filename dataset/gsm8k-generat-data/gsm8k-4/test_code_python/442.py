def solution():
    """Derek is watching the construction cranes downtown and is trying to figure out how much taller they have to be than the building they are building. He sees one crane that is 228 feet tall finishing a building that was 200 feet tall. He sees another that is 120 feet tall finishing a building that is 100 feet tall. The final crane he sees is 147 feet tall, finishing a building that is 140 feet tall. On average, what percentage taller are the cranes than the building?"""
    # Define the heights of the cranes and buildings
    crane_1_height = 228
    building_1_height = 200

    crane_2_height = 120
    building_2_height = 100

    crane_3_height = 147
    building_3_height = 140

    # Calculate the percentage taller of each crane compared to its building
    crane_1_percentage = ((crane_1_height - building_1_height) / building_1_height) * 100
    crane_2_percentage = ((crane_2_height - building_2_height) / building_2_height) * 100
    crane_3_percentage = ((crane_3_height - building_3_height) / building_3_height) * 100

    # Calculate the average percentage taller of the cranes compared to their buildings
    average_percentage = (crane_1_percentage + crane_2_percentage + crane_3_percentage) / 3

    # return the result
    result = average_percentage
    return result

print(solution())