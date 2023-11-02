def solution():
    total_loads = 8  # There are 8 loads of laundry to be washed
    wash_time = 0.75  # Each load takes 0.75 hours in the wash cycle (45 minutes)
    dry_time = 1  # Each load takes 1 hour in the dry cycle

    # Calculate the total time needed to wash and dry all the loads
    total_time = (wash_time + dry_time) * total_loads

    result = total_time
    return result

print(solution())