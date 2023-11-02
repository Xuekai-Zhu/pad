def solution():
    # Convert Keaton's ladder height to inches and calculate total climbed distance
    keaton_ladder = 30 * 12 # 30 feet converted to inches
    keaton_total_distance = keaton_ladder * 20

    # Calculate Reece's ladder height and convert to inches
    reece_ladder = (keaton_ladder - 4) * 12 # 4 feet shorter and converted to inches
    reece_total_distance = reece_ladder * 15

    # Calculate the total length of ladders climbed by both workers
    total_length = keaton_total_distance + reece_total_distance
    result = total_length
    return result

print(solution())