def solution():
    # Calculate the rate of typing for Meso and Tyler separately
    meso_rate = 15 / 5  # pages per minute
    tyler_rate = 15 / 3  # pages per minute

    # Calculate the combined rate of typing for Meso and Tyler
    combined_rate = meso_rate + tyler_rate

    # Calculate the time required to type 40 pages working together
    time = 40 / combined_rate

    result = time
    return result

print(solution())