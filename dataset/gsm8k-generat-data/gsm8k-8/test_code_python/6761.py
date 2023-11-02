def solution():
    # Define the length of the first show
    show1_length = 30

    # Define the length of the second show (4 times longer)
    show2_length = 4 * show1_length

    # Calculate the total length of time spent watching shows
    total_length = show1_length + show2_length

    # Convert the total length from minutes to hours (for output readability)
    total_length_hours = total_length / 60

    result = total_length_hours
    return result

print(solution())