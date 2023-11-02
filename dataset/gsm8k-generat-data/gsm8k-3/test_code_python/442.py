def solution():
   """Derek is watching the construction cranes downtown and is trying to figure out how much taller they have to be than the building they are building. He sees one crane that is 228 feet tall finishing a building that was 200 feet tall. He sees another that is 120 feet tall finishing a building that is 100 feet tall. The final crane he sees is 147 feet tall, finishing a building that is 140 feet tall. On average, what percentage taller are the cranes than the building?"""
    # Calculate the height differential and percentage increase for each crane
    diff1 = 228 - 200
    percent1 = (diff1 / 200) * 100
    diff2 = 120 - 100
    percent2 = (diff2 / 100) * 100
    diff3 = 147 - 140
    percent3 = (diff3 / 140) * 100

    # Calculate the average percentage increase of the cranes
    avg_percent = (percent1 + percent2 + percent3) / 3

    # Display the average percentage increase
    result = avg_percent
    return result

print(solution())