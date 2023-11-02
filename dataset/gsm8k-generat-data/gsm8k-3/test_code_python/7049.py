def solution():
    """James works for 240 minutes. He takes a water break every 20 minutes and a sitting break every 120 minutes. How many more water breaks does he take than sitting breaks?"""
    # Define the length of James's work shift in minutes
    work_shift = 240

    # Calculate the number of water breaks James takes
    water_breaks = work_shift // 20

    # Calculate the number of sitting breaks James takes
    sitting_breaks = work_shift // 120

    # Calculate the difference between the number of water breaks and sitting breaks
    difference = water_breaks - sitting_breaks

    # Display the difference
    result = difference
    return result

print(solution())