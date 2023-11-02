def solution():
    # Calculate the total length of commercials
    commercial_length = 10 * 3  # 3 commercials, each lasting 10 minutes
    total_length = 1.5  # total time of the TV show and commercials in hours
    tv_show_length = total_length - commercial_length/60  # calculate the length of the TV show itself
    result = tv_show_length
    return result

print(solution())