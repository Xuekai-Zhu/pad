def solution():
    """A local music festival is held every year for three days.  The three day attendance this year was 2700 people.  The second day was rainy so only half the number of people that showed up the first day showed up the second day.  The third day was the finale, so attendance was triple the original day.  How many people attended the second day of the festival?"""
    # Define the total attendance for the three days
    total_attendance = 2700

    # Calculate the attendance on the third day
    day3_attendance = total_attendance / 4 * 3

    # Calculate the attendance on the first day
    day1_attendance = (total_attendance - day3_attendance) / 2

    # Calculate the attendance on the second day
    day2_attendance = day1_attendance / 2

    # Display the attendance on the second day
    result = day2_attendance
    return result

print(solution())