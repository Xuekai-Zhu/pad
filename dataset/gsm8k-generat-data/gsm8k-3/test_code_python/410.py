def solution():
    """Mark wants to set the record for most consecutive ropes jumped.  The record is 54,000.  He can jump 3 times a second.  How many hours would he need to jump rope?"""
    # Define the number of jumps Mark can make in one second
    jumps_per_second = 3

    # Define the record number of consecutive jumps
    record_jumps = 54000

    # Calculate the time needed to jump the number of consecutive jumps in seconds
    time_in_seconds = record_jumps / jumps_per_second

    # Convert the time from seconds to hours
    time_in_hours = time_in_seconds / 3600

    # Display the time needed in hours
    result = time_in_hours
    return result

print(solution())