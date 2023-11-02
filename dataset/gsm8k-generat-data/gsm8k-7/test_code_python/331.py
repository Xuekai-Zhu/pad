def solution():
    road_length = 16

    # Calculate the total number of truckloads of asphalt needed to pave the road
    asphalt_truckloads = 3 * road_length

    # Calculate the total number of bags of gravel needed to make the asphalt
    gravel_bags = 2 * asphalt_truckloads

    # Calculate the total number of barrels of pitch needed to make the asphalt
    pitch_barrels = gravel_bags / 5

    # Calculate the number of miles paved on the first day
    miles_paved_day1 = 4

    # Calculate the number of miles paved on the second day
    miles_paved_day2 = (2 * miles_paved_day1) - 1

    # Calculate the total number of miles paved
    miles_paved = miles_paved_day1 + miles_paved_day2

    # Calculate the remaining number of miles to pave
    miles_remaining = road_length - miles_paved

    # Calculate the total number of truckloads of asphalt needed to pave the remaining road
    asphalt_truckloads_remaining = 3 * miles_remaining

    # Calculate the total number of bags of gravel needed to make the asphalt for the remaining road
    gravel_bags_remaining = 2 * asphalt_truckloads_remaining

    # Calculate the total number of barrels of pitch needed to make the asphalt for the remaining road
    pitch_barrels_remaining = gravel_bags_remaining / 5

    result = pitch_barrels_remaining
    return result

print(solution())