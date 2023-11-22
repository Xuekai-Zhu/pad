def solution():
    
    # Define the dimensions of each raised bed
    bed_width = 2
    bed_length = 8
    bed_height = 2

    # Calculate the volume of each raised bed
    bed_volume = bed_width * bed_length * bed_height

    # Calculate the total volume of raised beds
    total_bed_volume = 10 * bed_volume

    # Calculate the total volume of soil needed
    total_soil_volume = total_bed_volume * 2

    # Calculate the total cost of the soil
    total_cost = total_soil_volume * 12

    # return the result
    result = total_cost
    return result

print(solution())