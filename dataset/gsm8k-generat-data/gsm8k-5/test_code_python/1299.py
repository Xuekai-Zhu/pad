def solution():
    # Number of weeds pulled on Tuesday
    tuesday = 25

    # Number of weeds pulled on Wednesday
    wednesday = 3 * tuesday

    # Number of weeds pulled on Thursday
    thursday = wednesday / 5

    # Number of weeds pulled on Friday
    friday = thursday - 10

    # Total number of weeds pulled
    total_weeds = tuesday + wednesday + thursday + friday
    result = total_weeds
    return result

print(solution())