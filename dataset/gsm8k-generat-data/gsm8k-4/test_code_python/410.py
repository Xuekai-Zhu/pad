def solution():
    """Mark wants to set the record for most consecutive ropes jumped. The record is 54,000. He can jump 3 times a second. How many hours would he need to jump rope?"""
    # Define the number of rope jumps per second and the record number of jumps
    jumps_per_second = 3
    record_jumps = 54000

    # Calculate the total number of seconds required to beat the record
    seconds = record_jumps / jumps_per_second

    # Convert seconds to hours
    hours = seconds / 3600

    result = hours
    return result

print(solution())