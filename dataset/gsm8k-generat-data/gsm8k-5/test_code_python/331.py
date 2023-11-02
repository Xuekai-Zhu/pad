def solution():
    total_distance = 16  # The road is 16 miles long
    asphalt_per_mile = 3  # It takes 3 truckloads of asphalt to pave each mile of road
    gravel_per_asphalt = 2  # Each truckload of asphalt uses 2 bags of gravel
    pitch_per_gravel = 1/5  # Each truckload of asphalt uses 1 barrel of pitch for every 5 bags of gravel
    miles_day1 = 4  # The company paved 4 miles on the first day
    miles_day2 = (2 * miles_day1) - 1  # The company paved one mile less than double the distance paved on the first day

    # Calculate the total amount of asphalt, gravel, and pitch used on the first two days
    asphalt_total = asphalt_per_mile * (miles_day1 + miles_day2)
    gravel_total = 2 * asphalt_total  # Each truckload of asphalt uses 2 bags of gravel
    pitch_total = gravel_total * pitch_per_gravel  # Each truckload of asphalt uses 1 barrel of pitch for every 5 bags of gravel

    # Calculate the remaining distance and the amount of asphalt, gravel, and pitch needed to complete it
    remaining_distance = total_distance - (miles_day1 + miles_day2)
    remaining_asphalt = asphalt_per_mile * remaining_distance
    remaining_gravel = 2 * remaining_asphalt
    remaining_pitch = remaining_gravel * pitch_per_gravel

    # Calculate the amount of pitch needed on the third day
    pitch_day3 = remaining_pitch - pitch_total
    result = pitch_day3
    return result

print(solution())