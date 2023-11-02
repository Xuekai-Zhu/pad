def solution():
    # Calculate the total number of jumps Mark would need to beat the record
    jumps_needed = 54000  # the record is 54,000 consecutive jumps
    jumps_per_second = 3  # Mark can jump 3 times per second
    total_seconds = jumps_needed / jumps_per_second  # total seconds needed to complete the jumps
    hours_needed = total_seconds / 3600  # convert total seconds to hours
    result = hours_needed
    return result

print(solution())