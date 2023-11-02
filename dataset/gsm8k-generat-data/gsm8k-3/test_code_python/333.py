def solution():
    """A roadwork company is paving a newly constructed 16-mile road. They use a mixture of pitch and gravel to make the asphalt to pave the road. Each truckloads of asphalt uses two bags of gravel and five times as many bags of gravel as it does barrels of pitch to make. It takes three truckloads of asphalt to pave each mile of road. The company paved 4 miles of road on one day, then one mile less than double that on the second day. How many barrels of pitch will the company need to finish the remaining road on the third day?"""
    # Define the number of truckloads of asphalt needed for each mile of road
    TRUCKLOADS_PER_MILE = 3

    # Define the number of bags of gravel needed per barrel of pitch
    GRAVEL_PER_PITCH = 5

    # Define the number of bags of gravel needed per truckload of asphalt
    GRAVEL_PER_TRUCKLOAD = 2

    # Define the number of barrels of pitch needed per truckload of asphalt
    PITCH_PER_TRUCKLOAD = 1

    # Define the length of the road
    road_length = 16

    # Calculate the total number of truckloads of asphalt needed
    truckloads_needed = road_length * TRUCKLOADS_PER_MILE

    # Calculate the total number of bags of gravel needed
    gravel_needed = truckloads_needed * GRAVEL_PER_TRUCKLOAD

    # Calculate the total number of barrels of pitch needed
    pitch_needed = gravel_needed / GRAVEL_PER_PITCH

    # Calculate the number of miles paved on the first day
    miles_paved_day1 = 4

    # Calculate the number of miles paved on the second day
    miles_paved_day2 = (2 * miles_paved_day1) - 1

    # Calculate the number of miles left to pave
    miles_left_to_pave = road_length - miles_paved_day1 - miles_paved_day2

    # Calculate the number of truckloads of asphalt needed to finish the remaining road
    truckloads_needed_day3 = miles_left_to_pave * TRUCKLOADS_PER_MILE

    # Calculate the number of barrels of pitch needed to finish the remaining road
    pitch_needed_day3 = truckloads_needed_day3 * PITCH_PER_TRUCKLOAD

    # Add the pitch needed on day 3 to the total pitch needed
    total_pitch_needed = pitch_needed + pitch_needed_day3

    # Display the total number of barrels of pitch needed
    result = total_pitch_needed
    return result

print(solution())