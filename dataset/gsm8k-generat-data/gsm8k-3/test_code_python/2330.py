def solution():
    """James paints a 20 ft by 15 ft mural.  It takes him 20 minutes to paint 1 square foot and he charges $150 per hour.  How much does he charge to paint the mural?"""
    # Define the dimensions of the mural in square feet
    mural_area = 20 * 15

    # Calculate the time it takes James to paint the mural in hours
    time_hours = (mural_area * 20) / 60 / 60

    # Calculate James' total earnings for the job
    earnings = time_hours * 150

    # Display James' total earnings
    result = earnings
    return result

print(solution())