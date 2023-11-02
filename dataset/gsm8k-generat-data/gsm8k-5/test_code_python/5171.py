def solution():
    bed_length = 8  # Length of each raised bed is 8 feet
    bed_width = 4  # Width of each raised bed is 4 feet
    bed_height = 1  # Height of each raised bed is 1 foot

    # Calculate the volume of one raised bed
    bed_volume = bed_length * bed_width * bed_height

    # Calculate the total volume of both raised beds
    total_bed_volume = bed_volume * 2

    # Calculate the number of bags of soil needed
    bags_of_soil = total_bed_volume / 4  # Each bag of soil has 4 cubic feet

    result = bags_of_soil
    return result

print(solution())