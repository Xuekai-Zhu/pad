def solution():
    cans_per_half_hour = 30  # One machine produces 30 cans of soda every 30 minutes
    half_hours_per_hour = 2  # There are 2 half hours in an hour
    hours = 8  # Sue wants to know how many cans a machine can produce in 8 hours

    # Calculate the number of cans produced per hour by a machine
    cans_per_hour = cans_per_half_hour * half_hours_per_hour

    # Calculate the total number of cans produced by a machine in 8 hours
    total_cans = cans_per_hour * hours

    result = total_cans
    return result

print(solution())