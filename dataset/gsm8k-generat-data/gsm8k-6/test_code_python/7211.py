def solution():
    # Calculate the net length of ivy stripped every day
    net_ivy_length = 6 - 2  # Cary strips 6 feet of ivy everyday, but the ivy grows 2 feet every night

    # Calculate the number of days it will take Cary to strip all the ivy off
    days_taken = 40 / net_ivy_length

    result = days_taken
    return result

print(solution())