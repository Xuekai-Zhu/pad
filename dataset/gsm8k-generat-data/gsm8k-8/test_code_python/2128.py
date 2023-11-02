def solution():
    # Calculate the total amount of water needed for the students
    total_water_needed = 200 * 10

    # Calculate the number of jugs needed to hold the total water
    number_of_jugs = total_water_needed / 40

    # Round up to the nearest whole number of jugs
    number_of_jugs = math.ceil(number_of_jugs)

    result = number_of_jugs
    return result

print(solution())