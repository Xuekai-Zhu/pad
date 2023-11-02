def solution():
    """A roadwork company is paving a newly constructed 16-mile road. They use a mixture of pitch and gravel to make the asphalt to pave the road. Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make. It takes three truckloads of asphalt to pave each mile of road. The company paved 4 miles of road on one day, then one mile less than double that on the second day. How many barrels of pitch will the company need to finish the remaining road on the third day?"""
    # Define the total length of the road in miles and the number of truckloads needed to pave one mile
    total_miles = 16
    truckloads_per_mile = 3

    # Define the ratios of bags of gravel to barrels of pitch and the number of bags of gravel needed per truckload of asphalt
    gravel_to_pitch_ratio = 5
    bags_of_gravel_per_truckload = 2

    # Calculate the total number of truckloads of asphalt needed
    total_truckloads = total_miles * truckloads_per_mile

    # Calculate the total number of bags of gravel needed for all the truckloads of asphalt
    total_bags_of_gravel = total_truckloads * bags_of_gravel_per_truckload

    # Calculate the total number of barrels of pitch needed for all the truckloads of asphalt, using the ratio between bags of gravel and barrels of pitch
    total_barrels_of_pitch = total_bags_of_gravel / gravel_to_pitch_ratio

    # Calculate the number of miles of road paved on the first day
    miles_paved_day1 = 4

    # Calculate the number of miles of road paved on the second day (one mile less than double the first day's amount)
    miles_paved_day2 = (2 * miles_paved_day1) - 1

    # Calculate the total number of miles of road paved on the first two days
    total_miles_paved = miles_paved_day1 + miles_paved_day2

    # Calculate the remaining number of miles of road to pave
    miles_remaining = total_miles - total_miles_paved

    # Calculate the number of truckloads of asphalt needed to pave the remaining miles of road
    truckloads_remaining = miles_remaining * truckloads_per_mile

    # Calculate the number of bags of gravel needed for the remaining truckloads of asphalt
    bags_of_gravel_remaining = truckloads_remaining * bags_of_gravel_per_truckload

    # Calculate the number of barrels of pitch needed for the remaining bags of gravel, using the ratio between bags of gravel and barrels of pitch
    barrels_of_pitch_remaining = bags_of_gravel_remaining / gravel_to_pitch_ratio

    result = barrels_of_pitch_remaining
    return result

print(solution())