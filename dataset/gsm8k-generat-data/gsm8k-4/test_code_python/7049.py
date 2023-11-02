def solution():
    """James works for 240 minutes. He takes a water break every 20 minutes and a sitting break every 120 minutes. How many more water breaks does he take than sitting breaks?"""
    # Define the total working time and the break times
    total_time = 240
    water_break_time = 20
    sitting_break_time = 120

    # Calculate the number of breaks taken
    water_breaks = total_time // water_break_time
    sitting_breaks = total_time // sitting_break_time

    # Calculate the difference in the number of breaks taken
    difference = water_breaks - sitting_breaks

    result = difference
    return result

print(solution())