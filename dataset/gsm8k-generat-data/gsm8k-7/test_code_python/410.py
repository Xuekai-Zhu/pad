def solution():
    record = 54000
    jumps_per_second = 3

    # Calculate the total number of seconds it would take Mark to beat the record
    total_seconds = record / jumps_per_second

    # Convert the total seconds to hours
    total_hours = total_seconds / 3600
    result = total_hours
    return result

print(solution())