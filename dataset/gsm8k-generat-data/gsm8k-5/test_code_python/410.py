def solution():
    record = 54000  # The record for most consecutive ropes jumped is 54,000
    jumps_per_second = 3  # Mark can jump rope 3 times a second
    seconds_per_hour = 3600  # There are 3600 seconds in an hour

    # Calculate the number of hours Mark would need to jump rope to beat the record
    hours = record / (jumps_per_second * seconds_per_hour)
    result = hours
    return result

print(solution())