def solution():
    
    # Define the dimensions of each raised bed
    bed_width = 2
    bed_length = 8
    bed_height = 2

    # Calculate the volume of each raised bed
    bed_volume = bed_width * bed_length * bed_height

    # Calculate the total volume of all raised beds
    total_bed_volume = bed_volume * 10

    # Calculate the total volume of potting soil needed
    total_soil_volume = total_bed_volume * 2

    # Calculate the total cost of potting soil
    potting_soil_cost = total_soil_volume * 12

    # return the result
    result = potting_soil_cost
    return result

print(solution())