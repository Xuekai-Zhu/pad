def solution():
    bed_length = 8
    bed_width = 4
    bed_height = 1
    soil_bag_volume = 4

    # Calculate the volume of one bed
    bed_volume = bed_length * bed_width * bed_height

    # Calculate the total volume of both beds
    total_volume = bed_volume * 2

    # Calculate the number of soil bags needed
    num_bags = total_volume / soil_bag_volume
    result = num_bags
    return result

print(solution())